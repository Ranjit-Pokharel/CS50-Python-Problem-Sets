import pytest
from unittest.mock import patch, MagicMock
from project import (
    ArtificialIntelligence,
    take_user_input,
    clear_screen,
    requirement_check,
)
import os
import json
import subprocess

converse_path = "test_memory/test_conversation.json"
model = "llama3.2"


def test_ai_initialization():
    ai = ArtificialIntelligence(model=model, conversation_memory_file=converse_path)

    assert ai.model == model
    assert ai.conversation_memory_file == converse_path
    assert ai.system_edit == {}
    assert ai.conversation_datas == []


def test_load_memory():
    ai = ArtificialIntelligence(model=model, conversation_memory_file=converse_path)

    if os.path.exists(converse_path):
        os.remove(converse_path)
    ai.load_memory()
    assert ai.conversation_datas == []

    with open(converse_path, "w") as f:
        json.dump([{"user": "Hello", "ai": "Hi!"}], f)

    ai.load_memory()
    assert ai.conversation_datas == [{"user": "Hello", "ai": "Hi!"}]

    os.remove(converse_path)


def test_save_memory():
    ai = ArtificialIntelligence(model=model, conversation_memory_file=converse_path)
    ai.conversation_datas = [{"user": "How are you?", "ai": "I'm good, thanks!"}]
    ai.save_memory()

    with open(converse_path, "r") as f:
        saved_data = json.load(f)

    assert saved_data == ai.conversation_datas
    os.remove(converse_path)


def test_chat(monkeypatch):
    ai = ArtificialIntelligence(model=model, conversation_memory_file=converse_path)

    def mock_ollama_model(question):
        return "This is a mocked response."

    monkeypatch.setattr(ai, "chat", mock_ollama_model)

    response = ai.chat("Hello?")
    assert response == "This is a mocked response."


def test_system_level():
    ai = ArtificialIntelligence(
        model=model,
        conversation_memory_file=converse_path,
        system_edit={"role": "assistant", "content": ""},
    )

    ai.system_level()
    assert ai.system_edit == {"role": "assistant", "content": ""}


def test_clear_screen(monkeypatch):
    def mock_subprocess_call(command):
        if command == ["clear"]:
            return 0
        else:
            raise subprocess.CalledProcessError(1, command)

    monkeypatch.setattr("subprocess.call", mock_subprocess_call)

    result = clear_screen(["clear"])
    assert result == True, "Clear screen command failed"

    # Test the invalid command
    result = clear_screen(["invalid"])
    assert result == False, "Clear screen command should fail for an invalid command"


@patch("subprocess.run")  # Mocking subprocess.run
def test_requirement_check(mock_run):
    mock_run.return_value = MagicMock(
        returncode=0, stdout=b"/usr/bin/python3", stderr=b""
    )

    try:
        requirement_check("some_model")
    except SystemExit as e:
        pytest.fail(f"requirement_check failed: {e}")

    mock_run.return_value = MagicMock(returncode=1, stdout=b"", stderr=b"")

    with pytest.raises(SystemExit):
        requirement_check("some_model")

    mock_run.assert_any_call(["which", "python3"], capture_output=True)
    mock_run.assert_any_call(["which", "ollama"], capture_output=True)
    mock_run.assert_any_call(["ollama", "show", "some_model"], capture_output=True)


def test_take_user_input(monkeypatch):
    monkeypatch.setattr(
        "project.PromptSession.prompt", MagicMock(return_value="test input")
    )
    result = take_user_input("Enter something:")
    assert result == "test input", "User input was not captured correctly"
