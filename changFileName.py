import sys
from os import rename, listdir


folders = ['BOJ', 'JUNGOL', 'Programmers', 'SWEA']
folders_dict = {}
wrong_name = {
    'BOJ': [
        '[BAEKJOON]', '[BAKEJOON[', '[BAKEJOON]', '[BJ[', '[BJ] ', '[BJ ]', '[BJ]', '[BOJ[', '[BOJ] '
    ],
    'JUNGOL': [
        '[JUNGOL[', '[JUNGOL] ', '[JUNGOL[ '
    ],
    'Programmers': [
        '[프로그래머스]', '[KAKAO]', '[kakao]'
    ],
    'SWEA': [
        '[SWEA['
    ]
}

fix_name = {}


for folder in folders:
    folders_dict[folder] = listdir(f'./{folder}')
    fix_name[folder] = f'[{folder}]'


for folder_name, files in folders_dict.items():
    for name in files:
        for wrong in wrong_name[folder_name]:
            if wrong in name:
                new_name = name.replace(wrong, fix_name[folder_name])
                rename(f'./{folder_name}/{name}',
                       f'./{folder_name}/{new_name}')
                break
