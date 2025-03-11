import os
import subprocess
import sys
import logging
import time
import re

# 配置日志
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("WadHealthFixer")

def extract_wad_client(folder_path):
    """
    解包wad.client文件
    """
    logger.info("开始解包wad.client文件...")
    wad_extract_script = os.path.join(script_dir, "tools", "wad-extract-multi.bat")
    try:
        subprocess.check_call([wad_extract_script, folder_path])
        logger.info("完成解包wad.client文件。")
    except subprocess.CalledProcessError as e:
        logger.error(f"解包wad.client文件失败：{e}")

def make_wad_client(folder_path):
    """
    封包wad.client文件
    """
    logger.info("开始封包wad.client文件...")
    wad_make_script = os.path.join(script_dir, "tools", "wad-make-multi.bat")
    try:
        subprocess.check_call([wad_make_script, folder_path])
        logger.info("完成封包wad.client文件。")
    except subprocess.CalledProcessError as e:
        logger.error(f"封包wad.client文件失败：{e}")

def modify_py_content(py_content):
    # 使用正则表达式查找并替换所有形式的 "unitHealthBarStyle: u8 = 任何数字"
    pattern = r'unitHealthBarStyle: u8 = \d+'
    if re.search(pattern, py_content):
        # 如果存在，替换为新值
        py_content = re.sub(pattern, 'unitHealthBarStyle: u8 = 12', py_content)
        return py_content
    else:
        # 如果不存在，在 healthBarData 后面添加新的内容
        index = py_content.find("healthBarData")
        if index != -1:
            index = py_content.find("{", index)
            if index != -1:
                # 找到 '}' 的位置
                end_index = py_content.find("}", index)
                if end_index != -1:
                    # 在 '}' 前面插入新的内容
                    py_content = py_content[:end_index] + "\n    unitHealthBarStyle: u8 = 12" + py_content[end_index:]

    return py_content

def process_bin_files(folder_path):
    """
    处理bin文件
    """
    logger.info("开始处理bin文件...")
    wad_folders = [f for f in os.listdir(folder_path) if os.path.isdir(os.path.join(folder_path, f)) and ".wad" in f]

    for wad_folder in wad_folders:
        hero_path = os.path.join(folder_path, wad_folder, "data", "characters")
        if not os.path.exists(hero_path):
            logger.warning(f"在 {wad_folder} 中没有找到英雄文件夹。")
            continue

        hero_folders = os.listdir(hero_path)
        for hero_folder in hero_folders:
            skins_folder = os.path.join(folder_path, wad_folder, "data", "characters", hero_folder, "skins")
            if not os.path.exists(skins_folder):
                logger.warning(f"在 {hero_folder} 中没有找到皮肤文件夹。")
                continue

            bin_files = [f for f in os.listdir(skins_folder) if f.endswith(".bin")]

            for bin_file in bin_files:
                bin_file_path = os.path.join(skins_folder, bin_file)
                logger.info(f"处理文件：{bin_file_path}")

                try:
                    subprocess.check_call([bin_script, bin_file_path])
                    py_file_path = bin_file_path.replace(".bin", ".py")
                    with open(py_file_path, "r") as file:
                        py_content = file.read()

                    py_content = modify_py_content(py_content)

                    with open(py_file_path, "w") as file:
                        file.write(py_content)

                    subprocess.check_call([bin_script, py_file_path])
                    #os.remove(py_file_path)
                except subprocess.CalledProcessError as e:
                    logger.error(f"处理文件失败：{e}")

    logger.info("完成处理bin文件。")

def main():

    if not os.path.exists(bin_script):
        logger.error("bin文件夹路径不存在，请完整压本工具后再使用。")
        time.sleep(3)
        sys.exit(1)
    if not os.path.exists(wad_script):
        logger.error("tools文件夹路径不存在，请完整压本工具后再使用。")
        time.sleep(3)
        sys.exit(1)

    # 提示用户输入文件夹路径
    folder_path = input("请输入待修复的wad.client文件所在文件夹的路径(比如 D:\\test)：").strip()

    # 检查输入路径是否存在
    if not os.path.exists(folder_path):
        logger.error("指定的文件夹路径不存在，请重新输入。")
        time.sleep(3)
        sys.exit(1)

    extract_wad_client(folder_path)
    process_bin_files(folder_path)
    make_wad_client(folder_path)

    logger.error("指定文件夹中的wad文件已完成修复，5秒后程序将自动退出，感谢您的使用。")
    time.sleep(5)
    sys.exit(1)

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    bin_script = os.path.join(script_dir, "bin", "ritobin_cli.exe")
    wad_script = os.path.join(script_dir, "tools", "wad-extract.exe")
    main()
