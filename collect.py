# -*- coding=utf-8 -*-

import os
# from libs.io_helper import IOHelper

path = r'E:\a\aaa\video\jp\fc2'
txt = ''
t = []
t2 = []


def __loop(path, func):
    fs = os.listdir(path)
    for f in fs:
        func(path, f)


def collect(path):

    def func(path, fs):
        if fs != 'other':
            # print('fs:', fs, os.path.join(path, fs))
            full_path = os.path.join(path, fs)
            if os.path.isdir(full_path):
                global txt
                txt += fs + '\r'
                # print('fs,fp:', full_path)
                # t.append((fs, full_path))
                __loop(full_path, func)

    __loop(path, func)

    with open('./a.txt', 'w+', encoding='utf-8') as f:
        f.write(txt)

    # print(t)

    # for e in t:
    #     t2.append(e.replace(path + '\\', ''))

    # print(t2)

    # root = []
    # fs = os.listdir(path)

    # for f in fs:
    #     # f = os.path.join(path, f)
    #     root.append(f)
    #     fp = os.path.join(path, f)
    #     print('f,fp,isdir:', f, fp, os.path.isdir(fp))

    #     if os.path.isdir(fp):

    #         s1 = []
    #         fs2 = os.listdir(fp)

    #         for f2 in fs2:
    #             s1.append(f2)
    #             fp2 = os.path.join(fp, f2)
    #             print('f2,fp2,isdir:', f2, fp2, os.path.isdir(fp2))

    #             if os.path.isdir(fp2):

    #                 s2 = []
    #                 fs3 = os.listdir(fp2)

    #                 for f3 in fs3:
    #                     s2.append(f3)
    #                     fp3 = os.path.join(fp2, f3)
    #                     print('f3,fp3,isdir:', f3, fp3, os.path.isdir(fp3))

    #             else:
    #                 break

    #     else:
    #         break


collect(path)
