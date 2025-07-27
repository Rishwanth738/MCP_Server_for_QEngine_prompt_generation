def generate_prompt(task, context_chunks):
    formatted_functions = "\n".join(
        chunk for chunk in context_chunks if "zp_function_migrated" in chunk
    )

    context = formatted_functions if formatted_functions else "\n".join(context_chunks)

    prompt = (
        "You are an efficient QEngine script generator that generates QEngine scripts when given an image of the webpage and its HTML body.\n"
        "### INSTRUCTIONS:\n"
        "- DO NOT USE YOUR OWN LOGIC AND GENERATE A RAW SCRIPT.\n"
        "- Use only predefined functions, variables, and elements listed below.\n"
        "- Analyze the task and HTML body context to select the appropriate items.\n"
        "- DO NOT MAKE ANY ASSUMPTIONS unless instructed.\n\n"
        "---\n"
        "Context Functions & Elements:\n"
        f"{context}\n\n"
        "---\n"
        f"Task:\n{task}\n\n"
        "Output:\nQEngine script only, with proper structure.\n"
    )

    return prompt
