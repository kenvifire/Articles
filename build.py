import os
import sys
import json

def read_meta(file_path):
    start_str = '<!--'
    end_str = '-->'
    current_file = open(file_path, 'r')
    lines = current_file.readlines()
    count = 0
    closed = False
    meta_data = ''
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

walk_dir = sys.argv[1]

print('walk_dir = ' + walk_dir)

# If your current working directory may change during script execution, it's recommended to
# immediately convert program arguments to an absolute path. Then the variable root below will
# be an absolute path as well. Example:
# walk_dir = os.path.abspath(walk_dir)
print('walk_dir (absolute) = ' + os.path.abspath(walk_dir))
meta_file_path = os.path.join(walk_dir, 'blog_index.json')
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
                meta_content += meta_data + ","
if len(meta_content) > 1:
    meta_content = meta_content[:-1]
meta_content += ']'
meta_file.write(meta_content)
meta_file.close()













