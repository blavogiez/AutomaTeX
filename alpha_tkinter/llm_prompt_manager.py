# c:\Users\lab\Documents\BUT1\AutomaTeX\alpha_tkinter\llm_prompt_manager.py
"""
Manages loading and saving custom LLM prompt templates.

Prompts are saved on a per-document basis, allowing users to have
different prompt configurations for different projects.
"""
import json
import os

def get_prompts_filepath(tex_document_filepath):
    """Generates the filepath for the custom prompts JSON file."""
    if not tex_document_filepath:
        return None
    base, _ = os.path.splitext(tex_document_filepath)
    return f"{base}_prompts.json"

def save_prompts_to_file(prompts_dict, tex_document_filepath):
    """Saves the provided prompts dictionary to a JSON file."""
    prompts_filepath = get_prompts_filepath(tex_document_filepath)
    if not prompts_filepath:
        print("Debug: Not saving prompts as no .tex file path is available.")
        return
    try:
        with open(prompts_filepath, 'w', encoding='utf-8') as f:
            json.dump(prompts_dict, f, ensure_ascii=False, indent=4)
    except Exception as e:
        print(f"Error saving custom prompts to {prompts_filepath}: {e}")

def load_prompts_from_file(tex_document_filepath, default_prompts):
    """Loads custom prompts from a JSON file. If the file doesn't exist, it creates one with the default prompts."""
    prompts_filepath = get_prompts_filepath(tex_document_filepath)

    # If no file is open, just return the in-memory defaults
    if not prompts_filepath:
        return default_prompts

    if os.path.exists(prompts_filepath):
        try:
            with open(prompts_filepath, 'r', encoding='utf-8') as f:
                loaded_data = json.load(f)
                # Validate and merge with defaults to ensure all keys are present
                return {
                    "completion": loaded_data.get("completion", default_prompts["completion"]),
                    "generation": loaded_data.get("generation", default_prompts["generation"])
                }
        except Exception as e:
            print(f"Error loading custom prompts from {prompts_filepath}, using defaults. Error: {e}")
            return default_prompts # Fallback to defaults on error
    else:
        # File doesn't exist, so create it with default values
        print(f"Debug: Prompts file not found for {tex_document_filepath}. Creating with defaults.")
        save_prompts_to_file(default_prompts, tex_document_filepath)
        return default_prompts