"""
This module serves as the public-facing API (facade) for all Large Language Model (LLM) functionalities
within the application. It centralizes access to various LLM-related operations by delegating calls
to specialized internal modules, thereby promoting a clean, organized, and maintainable codebase.
"""

import llm_init
import llm_completion
import llm_generation
import llm_keywords
import llm_prompts
import llm_history

def initialize_llm_service(root_window, progress_bar_widget, theme_setting_getter, active_editor_getter, active_filepath_getter):
    """
    Initializes the entire LLM service by setting up core dependencies and loading initial data.

    This function acts as the primary entry point for setting up the LLM subsystem,
    passing necessary UI component references and getter functions to the underlying
    initialization module.

    Args:
        root_window (tk.Tk): The main Tkinter root window of the application.
        progress_bar_widget (ttk.Progressbar): The progress bar widget used to indicate LLM activity.
        theme_setting_getter (callable): A function to retrieve current theme settings.
        active_editor_getter (callable): A function to get the currently active editor widget.
        active_filepath_getter (callable): A function to get the file path of the active editor.
    """
    llm_init.initialize_llm_service(root_window, progress_bar_widget, theme_setting_getter, active_editor_getter, active_filepath_getter)

def load_prompts_for_current_file():
    """
    Loads the custom or default LLM prompt templates for the currently active document.

    This function delegates the loading process to the `llm_prompts` module,
    ensuring that the correct prompt configurations are available for the active file.
    """
    llm_prompts.load_prompts_for_current_file()

def open_set_keywords_dialog(event=None):
    """
    Opens the dialog for users to set or update global LLM keywords.

    This function acts as a wrapper, delegating the call to the `llm_keywords` module.

    Args:
        event (tk.Event, optional): The Tkinter event object, if called from a binding. Defaults to None.
    """
    llm_keywords.open_set_keywords_dialog()

def open_edit_prompts_dialog(event=None):
    """
    Opens the dialog for users to edit the LLM prompt templates.

    This function acts as a wrapper, delegating the call to the `llm_prompts` module.

    Args:
        event (tk.Event, optional): The Tkinter event object, if called from a binding. Defaults to None.
    """
    llm_prompts.open_edit_prompts_dialog()

def load_prompt_history_for_current_file():
    """
    Loads the LLM prompt and response history for the currently active document.

    This function delegates the loading process to the `llm_history` module,
    ensuring that the correct history is displayed for the active file.
    """
    llm_history.load_prompt_history_for_current_file()

def request_llm_to_complete_text(event=None):
    """
    Initiates a text completion request from the LLM based on the editor's content.

    This function acts as a wrapper, delegating the request to the `llm_completion` module.

    Args:
        event (tk.Event, optional): The Tkinter event object, if called from a binding. Defaults to None.
    """
    llm_completion.request_llm_to_complete_text()

def open_generate_text_dialog(event=None, initial_prompt_text=None):
    """
    Opens the dialog for custom text generation using the LLM.

    This function acts as a wrapper, delegating the call to the `llm_generation` module.
    It supports pre-filling the prompt text if `initial_prompt_text` is provided.

    Args:
        event (tk.Event, optional): The Tkinter event object, if called from a binding. Defaults to None.
        initial_prompt_text (str, optional): Initial text to pre-fill the prompt input area in the dialog.
                                             Defaults to None.
    """
    # The `event` parameter is included for consistency with shortcut bindings,
    # but it is not directly used by `llm_generation.open_generate_text_dialog`.
    llm_generation.open_generate_text_dialog(initial_prompt_text=initial_prompt_text)
