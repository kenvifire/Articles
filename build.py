import os
import sys
import json
import re

def read_meta(file_path):
    start_str = '<!--'
    end_str = '-->'
    current_file = open(file_path, 'r')
    lines = current_file.readlines()
    count = 0
    closed = False
    meta_data = ''
    ## need better way to get the settings
    for line in lines:
        line = line.strip()
        if count == 0:
            if line.startswith(start_str):
                meta_data += line[line.index(start_str)+4:]
                count += 1
                continue
            else:
                break

        if line.strip() == end_str:
            meta_data += line[:line.index(end_str)]
            closed = True
            break
        else:
            meta_data += line
        count += 1
    current_file.close()
    if closed:
        return meta_data

def find_pic(file_name):
    regex = r"!\[[^\]]*\]\((.*?)\s*(\"(?:.*[^\"])\")?\s*\)"
    file = open(file_name, 'r')
    pic = ''
    for line in file.readlines():
        matches = re.search(regex, line)
        if matches:
            pic = matches.group(1)
    file.close()
    return pic


    if closed:
        meta_json = json.loads(meta_data)
        meta_json['path'] = os.path.join(walk_dir, file_path)
        return meta_data

walk_dir = sys.argv[1]
build_dir = os.path.join(os.getcwd(), 'build')
print('walk_dir = ' + walk_dir)

if not os.path.exists(build_dir):
    os.makedirs(build_dir)
# If your current working directory may change during script execution, it's recommended to
# immediately convert program arguments to an absolute path. Then the variable root below will
# be an absolute path as well. Example:
# walk_dir = os.path.abspath(walk_dir)

print('walk_dir (absolute) = ' + os.path.abspath(walk_dir))
meta_file_path = os.path.join(walk_dir, build_dir, 'blog_index.json')
print(meta_file_path)
meta_file = open(meta_file_path, 'w')

meta_content = "["
for root, _, files in os.walk(walk_dir):

    for filename in files:
        if filename.endswith('.md'):
            file_path = os.path.join(root, filename)

            print('\t- file %s (full path: %s)' % (filename, file_path))
            meta_data = read_meta(file_path)


            if meta_data is not None:
                meta_json = json.loads(meta_data)
                meta_json['path'] = file_path
                meta_json['pic'] = find_pic(file_path)
                meta_content += json.dumps(meta_json) + ","
if len(meta_content) > 1:
    meta_content = meta_content[:-1]
meta_content += ']'
parsed_meta_content = json.loads(meta_content)
meta_file.write(json.dumps(parsed_meta_content, indent=4, sort_keys=True, ensure_ascii=False))
meta_file.close()














