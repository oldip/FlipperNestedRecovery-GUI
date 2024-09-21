import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.ttk import Progressbar
import subprocess
import threading
import os
import sys
import ctypes
import psutil
import re

# 定义多语言字典
translations = {
    'en': {
        'title': "FlipperNestedRecovery GUI 2.0",
        'uid': "UID",
        'port': "Port",
        'show_progress': "Show Progress",
        'enable_debug': "Enable Debug Mode",
        'save_nonces': "Save Nonces",
        'preserve_nonces': "Preserve Nonces",
        'nonces_file': "Nonces File",
        'browse': "Browse",
        'run': "Run",
        'stop': "Stop",
        'help': "Help",
        'uid_help': "UID: Unique identifier of the card. This is used to specify a specific card to analyze. Leave empty to analyze all cards.",
        'port_help': "Port: Communication port for Flipper. Set the port that your Flipper device is connected to. Leave empty for default.",
        'progress_help': "Show Progress: Displays the progress of the operation in real-time, allowing you to see the current status.",
        'debug_help': "Enable Debug Mode: Enable additional debugging options for advanced users.",
        'save_help': "Save Nonces: Save the nonces and keys from Flipper Zero to your computer for later analysis. This is useful for debugging and record-keeping.",
        'preserve_help': "Preserve Nonces: Preserve the nonces on Flipper Zero after recovering keys. Use this if you need to keep the nonces for future use.",
        'file_help': "Nonces File: Select a local .nonces file to recover keys from. This is used when you have saved nonces from a previous session.",
        'command_started': "Command execution started...",
        'command_finished': "Command execution finished with return code",
        'auto_selected': "Automatically selected option",
        'about': "About",
        'about_message': "Hello everyone, I am Oldip, a hacker who knows a little bit about everything and is very lazy. If you find any bugs during use, feel free to report them to me, but when I fix them is up to me (*^▽^*).\nThis is what happens when writing a program, you just need to run it, but Oldip has to consider many things o(╥﹏╥)o\n\nThis GUI version was not only developed based on AloneLiberty's original FlipperNestedRecovery, but also combined with the program itself, making it accessible for users who are not familiar with Python or who encountered installation failures.\n\nSpecial thanks to:\nZhaiRenGaiZaoJia: For providing the nonces files for testing and helping me test the bugs of this software.\nAloneLiberty: For developing the original FlipperNestedRecovery tool, on which this project is based.",
        'terminate_button_pressed': "Terminate button pressed",
        'process_terminated': "Subprocess has been successfully terminated",
        'terminate_failed': "Failed to terminate the process",
        'no_running_process': "No running subprocess",
        'output_hardnested_start': "[=] Hardnested attack starting...",
        'output_recovering_key': "Recovering key type {key_type}, sector {sector}",
        'output_found_key': "Found {count} key(s): {keys}",
        'output_found_potential_keys': "[+] Found potential {count} keys, use \"Check found keys\" in app (if using local nonces file, manually save the .keys file to Flipper Zero for \"Check found keys\" to work)",
        'output_saved_keys': "[?] Saved keys to",
        'output_nested_attack_delay': "[!] Nested attack with delay was used, will try more PRNG values (will take more time)",
        'output_select_depth': "[?] Please select depth of check",
        'output_option_fast': "[1] Fast: +-25 values",
        'output_option_normal': "[2] Normal: +-50 values",
        'output_option_full': "[3] Full: +-100 values [Recommended, ~2Gb RAM usage]",
        'output_option_custom': "[-] Custom [..any other value..]",
        'output_failed_find_keys': "[!] Failed to find keys for this sector, try running Nested attack again",
        'output_prompt': "[1-3/custom] > 3",
        'flipper_missing_error': "Flipper device is missing, unable to connect. Please ensure Flipper Zero is connected via USB and not occupied by other software (e.g., ./fbt log, qFlipper, lab.flipper.net).",
        'confirm_stop': "A cracking process is currently running. Are you sure you want to stop it?",
        'confirm_close': "A cracking process is currently running. Are you sure you want to close the application?",
        'output_key_recovery': "Key recovery",
    },
    'zh-cn': {
        'title': "FlipperNestedRecovery 图形用户界面 2.0",
        'uid': "UID",
        'port': "端口",
        'show_progress': "显示进度",
        'enable_debug': "启用调试模式",
        'save_nonces': "保存 Nonces",
        'preserve_nonces': "保留 Nonces",
        'nonces_file': "Nonces 文件",
        'browse': "浏览",
        'run': "运行",
        'stop': "停止",
        'help': "帮助",
        'uid_help': "UID: 卡片的唯一标识符。用于指定要分析的特定卡片。留空以分析所有卡片。",
        'port_help': "端口: Flipper 的通信端口。设置 Flipper 设备连接到的端口。留空为默认。",
        'progress_help': "显示进度: 在操作过程中实时显示进度。用户可以随时查看当前操作状态。",
        'debug_help': "启用调试模式: 为高级用户启用附加调试选项。",
        'save_help': "保存 Nonces: 将 Flipper Zero 上的 nonces 和 keys 保存到计算机，以便以后分析。这对于调试和记录非常有用。",
        'preserve_help': "保留 Nonces: 在恢复密钥后保留 Flipper Zero 上的 nonces。如果您需要保留 nonces 以供将来使用，请启用此选项。",
        'file_help': "Nonces 文件: 选择一个本地 .nonces 文件来恢复密钥。这在您保存了先前会话的 nonces 时使用。",
        'command_started': "命令执行已开始...",
        'command_finished': "命令执行已完成，返回代码",
        'auto_selected': "已自动选择选项",
        'about': "关于",
        'about_message': "大家好，我是老叶，一个什么都只懂一点点并且还非常懒的黑客。如果在使用途中发现任何bug，欢迎回报给我，而什么时候改就是我的事情了(*^▽^*)\n写程序是这样的，你们只要负责按运行就好了，而老叶要考虑的事情就多了\no(╥﹏╥)o\n\n此GUI版本不仅基于AloneLiberty原始的FlipperNestedRecovery开发，还将其程序结合在一起，使得不懂Python和安装失败的用户也能使用。\n\n特别鸣谢：\n宅人改造家：提供了nonces文件供我进行测试，并帮助我测试了软件的bug。\nAloneLiberty：感谢他开发了原始的FlipperNestedRecovery工具，本项目基于其工作进行开发。",
        'terminate_button_pressed': "终止按钮已按下",
        'process_terminated': "子进程已被成功终止",
        'terminate_failed': "无法终止进程",
        'no_running_process': "没有运行中的子进程",
        'output_hardnested_start': "[=] 强制嵌套攻击开始...",
        'output_recovering_key': "恢复密钥类型 {key_type}，扇区 {sector}",
        'output_found_key': "找到 {count} 个密钥: {keys}",
        'output_found_potential_keys': "[+] 找到 {count} 个潜在密钥，请在应用程序中使用\"检查电脑端破解出的秘钥\" (如果使用本地 nonces 文件破解，需要手动将 .keys 文件保存到 Flipper Zero 才可使用 \"检查电脑端破解出的秘钥\")",
        'output_saved_keys': "[?] 已保存密钥至",
        'output_nested_attack_delay': "[!] 使用了带延迟的嵌套攻击，将尝试更多的 PRNG 值（需要更多时间）",
        'output_select_depth': "[?] 请选择检查的深度",
        'output_option_fast': "[1] 快速：+-25 值",
        'output_option_normal': "[2] 正常：+-50 值",
        'output_option_full': "[3] 完全：+-100 值 [推荐，约 2Gb RAM 使用量]",
        'output_option_custom': "[-] 自定义 [..任何其他值..]",
        'output_failed_find_keys': "[!] 未能找到该扇区的密钥，再次尝试运行嵌套攻击",
        'output_prompt': "[1-3/自定义] > 3",
        'flipper_missing_error': "Flipper 设备丢失，无法连接。请确保 Flipper Zero 通过 USB 线连接，并且没有被任何其他软件（例如 ./fbt log、qFlipper、lab.flipper.net）占用。",
        'confirm_stop': "当前正在执行破解操作。您确定要停止吗？",
        'confirm_close': "当前正在执行破解操作。您确定要关闭程序吗？",
        'output_key_recovery': "密钥恢复进度",
    },
    'zh-tw': {
        'title': "FlipperNestedRecovery 圖形用戶界面 2.0",
        'uid': "UID",
        'port': "端口",
        'show_progress': "顯示進度",
        'enable_debug': "啟用調試模式",
        'save_nonces': "保存 Nonces",
        'preserve_nonces': "保留 Nonces",
        'nonces_file': "Nonces 文件",
        'browse': "瀏覽",
        'run': "運行",
        'stop': "停止",
        'help': "幫助",
        'uid_help': "UID: 卡片的唯一標識符。用於指定要分析的特定卡片。留空以分析所有卡片。",
        'port_help': "端口: Flipper 的通信端口。設置 Flipper 設備連接到的端口。留空為默認。",
        'progress_help': "顯示進度: 在操作過程中實時顯示進度。用戶可以隨時查看當前操作狀態。",
        'debug_help': "啟用調試模式: 為高級用戶啟用附加調試選項。",
        'save_help': "保存 Nonces: 將 Flipper Zero 上的 nonces 和 keys 保存到計算機，以便以後分析。這對於調試和記錄非常有用。",
        'preserve_help': "保留 Nonces: 在恢復密鑰後保留 Flipper Zero 上的 nonces。如果您需要保留 nonces 以供將來使用，請啟用此選項。",
        'file_help': "Nonces 文件: 選擇一個本地 .nonces 文件來恢復密鑰。這在您保存了先前會話的 nonces 時使用。",
        'command_started': "命令執行已開始...",
        'command_finished': "命令執行已完成，返回代碼",
        'auto_selected': "已自動選擇選項",
        'about': "關於",
        'about_message': "大家好，我是老葉，一個什麼都只懂一點點並且還非常懶的黑客。如果在使用途中發現任何bug，歡迎回報給我，而什麼時候改就是我的事情了(*^▽^*)\n寫程序是這樣的，你們只要負責按運行就好了，而老葉要考慮的事情就多了\no(╥﹏╥)o\n\n此GUI版本不僅基於AloneLiberty的原始FlipperNestedRecovery開發，還將其程序結合在一起，使得不懂Python和安裝失敗的用戶也能使用。\n\n特別鳴謝：\n宅人改造家：提供了nonces文件供我進行測試，並幫助我測試了軟件的bug。\nAloneLiberty：感謝他開發了原始的FlipperNestedRecovery工具，本項目基於其工作進行開發。",
        'terminate_button_pressed': "終止按鈕已按下",
        'process_terminated': "子進程已被成功終止",
        'terminate_failed': "無法終止進程",
        'no_running_process': "沒有運行中的子進程",
        'output_hardnested_start': "[=] 強制嵌套攻擊開始...",
        'output_recovering_key': "恢復密鑰類型 {key_type}，扇區 {sector}",
        'output_found_key': "找到 {count} 個密鑰: {keys}",
        'output_found_potential_keys': "[+] 找到 {count} 個潛在密鑰，請在應用程序中使用\"檢查電腦端破解出的秘鑰\" (如果使用本地 nonces 文件破解，需要手動將 .keys 文件保存到 Flipper Zero 才可使用 \"檢查電腦端破解出的秘鑰\")",
        'output_saved_keys': "[?] 已保存密鑰至",
        'output_nested_attack_delay': "[!] 使用了帶延遲的嵌套攻擊，將嘗試更多的 PRNG 值（需要更多時間）",
        'output_select_depth': "[?] 請選擇檢查的深度",
        'output_option_fast': "[1] 快速：+-25 值",
        'output_option_normal': "[2] 正常：+-50 值",
        'output_option_full': "[3] 完全：+-100 值 [推薦，約 2Gb RAM 使用量]",
        'output_option_custom': "[-] 自定義 [..任何其他值..]",
        'output_failed_find_keys': "[!] 未能找到該扇區的密鑰，再次嘗試運行嵌套攻擊",
        'output_prompt': "[1-3/自定義] > 3",
        'flipper_missing_error': "Flipper 設備丟失，無法連接。請確保 Flipper Zero 通過 USB 線連接，並且沒有被任何其他軟件（例如 ./fbt log、qFlipper、lab.flipper.net）佔用。",
        'confirm_stop': "當前正在執行破解操作。您確定要停止嗎？",
        'confirm_close': "當前正在執行破解操作。您確定要關閉程式嗎？",
        'output_key_recovery': "密鑰恢復進度",
    }
}

# 设置初始语言为简体中文
current_language = 'zh-cn'
process = None

def set_language(lang):
    global current_language
    current_language = lang
    update_labels()

def update_labels():
    lang = translations[current_language]
    root.title(lang['title'])
    uid_label.config(text=lang['uid'])
    port_label.config(text=lang['port'])
    show_progress_check.config(text=lang['show_progress'])
    enable_debug_check.config(text=lang['enable_debug'])
    save_check.config(text=lang['save_nonces'])
    preserve_check.config(text=lang['preserve_nonces'])
    file_label.config(text=lang['nonces_file'])
    browse_button.config(text=lang['browse'])
    run_button.config(text=lang['run'])
    stop_button.config(text=lang['stop'])
    uid_help_button.config(command=lambda: show_help(lang['uid_help']))
    port_help_button.config(command=lambda: show_help(lang['port_help']))
    progress_help_button.config(command=lambda: show_help(lang['progress_help']))
    debug_help_button.config(command=lambda: show_help(lang['debug_help']))
    save_help_button.config(command=lambda: show_help(lang['save_help']))
    preserve_help_button.config(command=lambda: show_help(lang['preserve_help']))
    file_help_button.config(command=lambda: show_help(lang['file_help']))
    about_button.config(text=lang['about'])

def show_about():
    lang = translations[current_language]
    messagebox.showinfo(lang['about'], lang['about_message'])
    
def confirm_and_stop():
    lang = translations[current_language]
    confirm = messagebox.askyesno("Confirm Stop", lang['confirm_stop'])
    if confirm:
        stop_subprocess()

def stop_subprocess():
    global process
    lang = translations[current_language]
    if process is not None:
        append_to_output(f"{lang['terminate_button_pressed']}\n")
        try:
            parent = psutil.Process(process.pid)
            for child in parent.children(recursive=True):  # 终止所有子进程
                child.terminate()
            parent.terminate()
            parent.wait()  # 等待父进程和所有子进程结束
            append_to_output(f"{lang['process_terminated']}\n")
        except Exception as e:
            messagebox.showerror("Error", f"{lang['terminate_failed']}: {str(e)}\n")
        process = None  # 重置process变量以防止重复终止操作
    else:
        append_to_output(f"{lang['no_running_process']}\n")

def on_closing():
    global process
    lang = translations[current_language]
    if process is not None:
        confirm = messagebox.askyesno("Confirm Close", lang['confirm_close'])
        if not confirm:
            return
    stop_subprocess()  # 终止子进程
    # 尝试停止其他可能阻塞的线程
    root.quit()  # 停止事件循环
    root.destroy()  # 销毁窗口

def append_to_output(text):
    output_text.config(state=tk.NORMAL)  # 允许写入
    output_text.insert(tk.END, text)
    output_text.see(tk.END)  # 滚动到最后一行
    output_text.config(state=tk.DISABLED)  # 再次禁用编辑

# 设置窗口的初始大小并禁用最大化按钮
def disable_maximize_button():
    root.update_idletasks()
    hwnd = ctypes.windll.user32.GetParent(root.winfo_id())
    style = ctypes.windll.user32.GetWindowLongW(hwnd, -16)
    style &= ~0x00010000  # 禁用最大化按钮
    ctypes.windll.user32.SetWindowLongW(hwnd, -16, style)

def disable_window_resize():
    root.resizable(False, False)  # 禁用手动调整窗口大小
    disable_maximize_button()  # 禁用最大化按钮

# 动态调整窗口大小的函数
def temporary_resize_window(width_change, height_change):
    # 直接获取当前窗口大小，不调用 update_idletasks
    current_width = root.winfo_width()
    current_height = root.winfo_height()

    # 计算新的窗口大小
    new_width = current_width + width_change
    new_height = current_height + height_change
    
    # 设置新的窗口大小
    root.geometry(f"{new_width}x{new_height}")

def run_flippernested(uid, port, show_progress, save_nonces, preserve_nonces, file_path):
    global process
    flipper_exe = os.path.join(sys._MEIPASS, 'FlipperNestedRecovery 2.0.exe')
    cmd = [flipper_exe]
    if uid:
        cmd.append(f'--uid {uid}')
    if port:
        cmd.append(f'--port {port}')
    if show_progress:
        cmd.append('--progress')
    if save_nonces:
        cmd.append('--save')
    if preserve_nonces:
        cmd.append('--preserve')
    if file_path:
        cmd.append(f'--file "{file_path.replace("\\", "/")}"')

    cmd = " ".join(cmd)

    def read_process_output(process):
        while True:
            lang = translations[current_language]
            output = process.stdout.readline()
            if output == "" and process.poll() is not None:
                break
            if output:
                # 如果输出包含 "[1-3/custom] >" 和 "Recovering key type"，将其分割并分别处理
                if "[1-3/custom] >" in output and "Recovering key type" in output:
                    # 分割输出内容
                    parts = output.split("> ")
                    prompt_part = parts[0] + ">"
                    recovery_part = "> ".join(parts[1:])

                    # 翻译提示部分
                    translated_prompt = prompt_part.replace("[1-3/custom] >", lang['output_prompt'])
                    append_to_output(translated_prompt + "\n")
                    
                    # 翻译恢复密钥部分
                    match = re.match(r"Recovering key type (\w+), sector (\d+)", recovery_part)
                    if match:
                        key_type, sector = match.groups()
                        translated_recovery = lang['output_recovering_key'].format(key_type=key_type, sector=sector) + "\n"
                        append_to_output(translated_recovery)
                    continue
                
                # 如果是单独的 "[1-3/custom] >"，则翻译它
                elif "[1-3/custom] >" in output:
                    output = output.replace("[1-3/custom] >", lang['output_prompt'] + "\n")

                # 如果输出包含 "Key recovery:" 和 "Found "，将其使用")"分割并分别处理
                elif "Key recovery:" in output and "Found " in output:
                    # 使用第一个")"分割输出内容
                    parts = output.split(")", 1)
                    found_part = parts[1]
                    
                    # 翻译找到密钥的部分
                    match = re.match(r"Found (\d+) key\(s\): (\[.*\])", found_part)
                    if match:
                        count, keys = match.groups()
                        translated_recovery = lang['output_found_key'].format(count=count, keys=keys) + "\n"
                        output_text.config(state=tk.NORMAL)
                        output_text.delete("end-2l", "end-1l")  # 删除最后一行
                        output_text.insert(tk.END, translated_recovery)  # 插入新的进度条内容
                        output_text.config(state=tk.DISABLED)
                    continue

                # 如果是"Key recovery:"，则替换最后一行
                elif "Key recovery:" in output:
                    output = output.replace("Key recovery", lang['output_key_recovery'])
                    output_text.config(state=tk.NORMAL)
                    output_text.delete("end-2l", "end-1l")  # 删除最后一行
                    output_text.insert(tk.END, output)  # 插入新的内容
                    output_text.config(state=tk.DISABLED)
                    continue
                # 翻译指定内容
                elif "[=] Hardnested attack starting..." in output:
                    output = lang['output_hardnested_start'] + "\n"
                elif "Recovering key type" in output and "sector" in output:
                    match = re.match(r"Recovering key type (\w+), sector (\d+)", output)
                    if match:
                        key_type, sector = match.groups()
                        output = lang['output_recovering_key'].format(key_type=key_type, sector=sector) + "\n"
                elif "Found " in output and "key(s):" in output:
                    match = re.match(r"Found (\d+) key\(s\): (\[.*\])", output)
                    if match:
                        count, keys = match.groups()
                        output = lang['output_found_key'].format(count=count, keys=keys) + "\n"
                elif "[+] Found potential" in output:
                    match = re.match(r"\[\+\] Found potential (\d+) keys", output)
                    if match:
                        count = match.group(1)
                        output = lang['output_found_potential_keys'].format(count=count) + "\n"
                elif "[?] Saved keys to" in output:
                    output = output.replace("[?] Saved keys to", lang['output_saved_keys'])
                elif "[!] Nested attack with delay was used" in output:
                    output = lang['output_nested_attack_delay'] + "\n"
                elif "[?] Please select depth of check" in output:
                    output = lang['output_select_depth'] + "\n"
                elif "[1] Fast: +-25 values" in output:
                    output = lang['output_option_fast'] + "\n"
                elif "[2] Normal: +-50 values" in output:
                    output = lang['output_option_normal'] + "\n"
                elif "[3] Full: +-100 values" in output:
                    output = lang['output_option_full'] + "\n"
                elif "[-] Custom [..any other value..]" in output:
                    append_to_output(lang['output_option_custom'] + "\n")
                    # 检测到提示选择的情况，自动选择 "3"
                    process.stdin.write("3\n")
                    process.stdin.flush()
                    append_to_output(f"{lang['auto_selected']} 3\n")
                    continue

                elif "[!] Failed to find keys for this sector" in output:
                    output = lang['output_failed_find_keys'] + "\n"
                
                append_to_output(output)

    try:
        lang = translations[current_language]
        append_to_output(f"{lang['command_started']}\n")
        progress_bar.grid(row=7, column=1, columnspan=4, padx=0, pady=10, sticky="ew")
        progress_bar.start()
        
        # 调整窗口高度
        temporary_resize_window(0, 50)

        # 使用 CREATE_NO_WINDOW 来隐藏命令行窗口
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE, text=True, creationflags=subprocess.CREATE_NO_WINDOW, bufsize=1, universal_newlines=True)

        # 启动子线程
        thread = threading.Thread(target=read_process_output, args=(process,))
        thread.start()

        # 等待子线程完成
        thread.join()
        
        if process is not None:
            rc = process.poll()
            lang = translations[current_language]
            append_to_output(f"{lang['command_finished']} {rc}\n")

        # 检查 process 是否为 None 以防止 NoneType 错误
        if process and process.stderr:
            try:
                stderr_output = process.stderr.read()
                if stderr_output:
                    if "ConnectionError: Flipper is missing" in stderr_output:
                        lang = translations[current_language]
                        messagebox.showerror("Error", lang['flipper_missing_error'])
                        append_to_output(f"{lang['flipper_missing_error']}\n")
                        return
                    else:
                        messagebox.showerror("Error", stderr_output)
                    append_to_output(f"{stderr_output}\n")
            except Exception as e:
                append_to_output(f"Error reading stderr: {str(e)}\n")
            
    except Exception as e:
        messagebox.showerror("Error", str(e))
        append_to_output(f"{str(e)}\n")
    finally:
        process = None
        progress_bar.stop()
        temporary_resize_window(0, -50)
        progress_bar.grid_remove()
        enable_widgets()

def open_file_dialog():
    file_path = filedialog.askopenfilename()
    file_entry.config(state=tk.NORMAL)
    file_entry.delete(0, tk.END)
    file_entry.insert(0, file_path.replace("\\", "/"))
    file_entry.config(state=tk.DISABLED)

def toggle_debug_mode():
    debug = debug_var.get()
    if debug:
        save_check.grid(row=3, column=1, padx=10, pady=10, sticky="w")
        save_help_button.grid(row=3, column=2, padx=1, pady=10, sticky="w")
        preserve_check.grid(row=3, column=4, padx=10, pady=10, sticky="w")
        preserve_help_button.grid(row=3, column=5, padx=1, pady=10, sticky="w")
        file_label.grid(row=4, column=1, padx=5, pady=10, sticky="w")
        file_entry.grid(row=4, column=2, columnspan=2, padx=0, pady=10, sticky="w")
        browse_button.grid(row=4, column=4, padx=10, pady=10, sticky="w")
        file_help_button.grid(row=4, column=5, padx=1, pady=10, sticky="w")
        temporary_resize_window(0, 100)
    else:
        save_check.grid_remove()
        save_help_button.grid_remove()
        preserve_check.grid_remove()
        preserve_help_button.grid_remove()
        file_label.grid_remove()
        file_entry.grid_remove()
        browse_button.grid_remove()
        file_help_button.grid_remove()
        temporary_resize_window(0, -100)

def show_help(message):
    lang = translations[current_language]
    messagebox.showinfo(lang['help'], message)

def disable_widgets():
    uid_entry.config(state=tk.DISABLED)
    port_entry.config(state=tk.DISABLED)
    show_progress_check.config(state=tk.DISABLED)
    enable_debug_check.config(state=tk.DISABLED)
    save_check.config(state=tk.DISABLED)
    preserve_check.config(state=tk.DISABLED)
    file_entry.config(state=tk.DISABLED)
    browse_button.config(state=tk.DISABLED)
    run_button.config(state=tk.DISABLED)
    stop_button.config(state=tk.NORMAL)  # 啟用停止按鈕

def enable_widgets():
    uid_entry.config(state=tk.NORMAL)
    port_entry.config(state=tk.NORMAL)
    show_progress_check.config(state=tk.NORMAL)
    enable_debug_check.config(state=tk.NORMAL)
    save_check.config(state=tk.NORMAL)
    preserve_check.config(state=tk.NORMAL)
    file_entry.config(state=tk.NORMAL)
    browse_button.config(state=tk.NORMAL)
    run_button.config(state=tk.NORMAL)
    stop_button.config(state=tk.DISABLED)  # 禁用停止按鈕

def run_in_thread():
    uid = uid_entry.get()
    port = port_entry.get()
    show_progress = progress_var.get()
    save_nonces = save_var.get()
    preserve_nonces = preserve_var.get()
    file_path = file_entry.get() if file_entry.get() else None
    disable_widgets()
    thread = threading.Thread(target=run_flippernested, args=(uid, port, show_progress, save_nonces, preserve_nonces, file_path))
    thread.daemon = True  # 设置线程为守护线程
    thread.start()

root = tk.Tk()
root.iconbitmap(os.path.join(sys._MEIPASS, 'hacker.ico'))

root.update_idletasks()
# 禁用手动调整窗口大小和最大化按钮
disable_window_resize()

# 语言选择
language_var = tk.StringVar(value=current_language)
language_menu = tk.OptionMenu(root, language_var, 'en', 'zh-cn', 'zh-tw', command=set_language)
language_menu.grid(row=0, column=5, padx=5, pady=10, sticky="e")

# UID 和 Port 输入框并排放置
uid_label = tk.Label(root, text="UID")
uid_label.grid(row=1, column=0, padx=10, pady=10, sticky="e")
uid_entry = tk.Entry(root, width=20)  # 调整宽度
uid_entry.grid(row=1, column=1, padx=10, pady=10, sticky="w")
uid_help_button = tk.Button(root, text="?")
uid_help_button.grid(row=1, column=2, padx=1, pady=10, sticky="w")

port_label = tk.Label(root, text="Port")
port_label.grid(row=1, column=3, padx=10, pady=10, sticky="e")
port_entry = tk.Entry(root, width=20)  # 调整宽度
port_entry.grid(row=1, column=4, padx=10, pady=10, sticky="w")
port_help_button = tk.Button(root, text="?")
port_help_button.grid(row=1, column=5, padx=1, pady=10, sticky="w")

# Progress 和 Debug 复选框并排放置
progress_var = tk.BooleanVar(value=True)
show_progress_check = tk.Checkbutton(root, text="Show Progress", variable=progress_var)
show_progress_check.grid(row=2, column=1, padx=10, pady=10, sticky="w")
progress_help_button = tk.Button(root, text="?")
progress_help_button.grid(row=2, column=2, padx=1, pady=10, sticky="w")

debug_var = tk.BooleanVar()
enable_debug_check = tk.Checkbutton(root, text="Enable Debug Mode", variable=debug_var, command=toggle_debug_mode)
enable_debug_check.grid(row=2, column=4, padx=10, pady=10, sticky="w")
debug_help_button = tk.Button(root, text="?")
debug_help_button.grid(row=2, column=5, padx=1, pady=10, sticky="w")

# Save Nonces 和 Preserve Nonces 复选框在同一行
save_var = tk.BooleanVar()
save_check = tk.Checkbutton(root, text="Save Nonces", variable=save_var)
save_check.grid(row=3, column=1, padx=10, pady=10, sticky="w")
save_check.grid_remove()
save_help_button = tk.Button(root, text="?")
save_help_button.grid(row=3, column=2, padx=1, pady=10, sticky="w")
save_help_button.grid_remove()

preserve_var = tk.BooleanVar()
preserve_check = tk.Checkbutton(root, text="Preserve Nonces", variable=preserve_var)
preserve_check.grid(row=3, column=4, padx=10, pady=10, sticky="w")
preserve_check.grid_remove()
preserve_help_button = tk.Button(root, text="?")
preserve_help_button.grid(row=3, column=5, padx=1, pady=10, sticky="w")
preserve_help_button.grid_remove()


# Nonces File 选择
file_label = tk.Label(root, text="Nonces File")
file_label.grid(row=4, column=1, padx=5, pady=10, sticky="w")
file_label.grid_remove()

file_entry = tk.Entry(root, width=25)
file_entry.grid(row=4, column=2, columnspan=2, padx=0, pady=10, sticky="w")
file_entry.grid_remove()

browse_button = tk.Button(root, text="Browse", command=open_file_dialog)
browse_button.grid(row=4, column=4, padx=10, pady=10, sticky="w")
browse_button.grid_remove()
file_help_button = tk.Button(root, text="?")
file_help_button.grid(row=4, column=5, padx=1, pady=10, sticky="w")
file_help_button.grid_remove()

# Run 和 Stop 按鈕
run_button = tk.Button(root, text="Run", command=run_in_thread, width=20)
run_button.grid(row=5, column=1, columnspan=2, padx=10, pady=20)

stop_button = tk.Button(root, text="Stop", command=confirm_and_stop, state=tk.DISABLED, width=20)
stop_button.grid(row=5, column=4, columnspan=2, padx=10, pady=20, sticky="w")


# 进度条
progress_bar = Progressbar(root, mode='indeterminate', length=600)
progress_bar.grid(row=7, column=1, columnspan=4, padx=0, pady=10, sticky="ew")
progress_bar.grid_remove()


# 创建输出文本框和滚动条
output_text_frame = tk.Frame(root)  # 创建一个框架来包含文本和滚动条
output_text_frame.grid(row=6, column=0, columnspan=6, padx=5, pady=10, sticky="ew")

output_text = tk.Text(output_text_frame, wrap=tk.WORD, height=15, width=107, state=tk.DISABLED)
output_text.grid(row=0, column=0, sticky="nsew")

scrollbar = tk.Scrollbar(output_text_frame, orient=tk.VERTICAL, command=output_text.yview)
scrollbar.grid(row=0, column=1, sticky="ns")

output_text.config(yscrollcommand=scrollbar.set)

# 保持Text小部件和滚动条一起伸展
output_text_frame.grid_rowconfigure(0, weight=1)
output_text_frame.grid_columnconfigure(0, weight=1)


# 关于按钮
about_button = tk.Button(root, text="About", command=show_about, width=35)
about_button.grid(row=8, column=1, columnspan=4, padx=10, pady=10)

update_labels()  # 初始化标签

# 添加窗口关闭事件
root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()