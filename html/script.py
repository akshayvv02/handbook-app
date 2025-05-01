import os

def clean_html_files_in_current_folder():
    current_dir = os.getcwd()
    changed = False

    for filename in os.listdir(current_dir):
        if filename.endswith('.html'):
            file_path = os.path.join(current_dir, filename)

            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            # Save old for comparison
            original_content = content

            # Apply replacements
            content = content.replace('role + "_" + wtd;', 'role + "_" + wtd + ".html";')
            #content = content.replace("') }}", "")

            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"✅ Cleaned: {filename}")
                changed = True

    if not changed:
        print("⚠️ No .html files were changed — check content or pattern.")
    else:
        print("✔️ Done cleaning .html files.")

clean_html_files_in_current_folder()
