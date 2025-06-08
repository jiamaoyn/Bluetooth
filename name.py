import os

# 设置你的目标文件夹路径
TARGET_FOLDER = "/Users/wangjiamao/code/esp32s3/mp3qq/U盘/mp3"

def rename_mp3_files(folder):
    files = [f for f in os.listdir(folder) if f.lower().endswith('.mp3')]
    files.sort()  # 默认按文件名排序；可改为 sorted(..., key=lambda f: os.path.getmtime(os.path.join(folder, f))) 按修改时间

    for i, old_name in enumerate(files, start=1):
        new_name = f"{i:04}.mp3"
        old_path = os.path.join(folder, old_name)
        new_path = os.path.join(folder, new_name)

        if old_path == new_path:
            print(f"✅ 已正确命名: {old_name}")
            continue

        # 如果目标文件名已存在，先删除或重命名防冲突（可选）
        if os.path.exists(new_path):
            print(f"⚠️ 文件已存在，跳过: {new_name}")
            continue

        os.rename(old_path, new_path)
        print(f"✅ 重命名: {old_name} → {new_name}")

if __name__ == "__main__":
    rename_mp3_files(TARGET_FOLDER)
