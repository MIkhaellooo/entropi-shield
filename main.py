import psutil
import time
import hashlib
from nicegui import ui

def get_thermal():
    try:
        get_data = psutil.sensors_temperatures()
        select_data = get_data['coretemp']
        default = ""
        for i, entry in enumerate(select_data):
            print(i, entry)
            time_now = str(time.time_ns())[:-3]
            temp_now = str(entry.current).replace(".", "")
            default += time_now + temp_now
        return default
    except Exception:
        return None

def refresh_data():
    raw_data = get_thermal()
    if raw_data:
        token = hashlib.sha256(raw_data.encode()).hexdigest()
        token_label.set_text(token)
        time_label.set_text(f"Last Update: {time.strftime('%H:%M:%S')}")

ui.query('body').classes('bg-slate-900 text-white font-sans')

with ui.column().classes('w-full items-center p-10 gap-6'):
    
    ui.label('ENTROPY SHIELD').classes('text-4xl font-black text-blue-500 tracking-tighter')

    with ui.card().classes('bg-slate-800/50 border border-slate-700 backdrop-blur-md p-8 rounded-2xl shadow-2xl w-full max-w-2xl'):
        ui.label('Hardware Generated Token').classes('text-xs font-bold text-slate-400 tracking-widest mb-2')

        token_label = ui.label('Waiting...').classes('text-green-400 font-mono break-all bg-black/40 p-4 rounded-lg border border-green-900/30')
        
        with ui.row().classes('w-full justify-between items-center mt-6'):
            time_label = ui.label('Last Update: --:--:--').classes('text-slate-500 text-sm italic')
            ui.button('REFRESH', on_click=refresh_data).classes('bg-blue-600 hover:bg-blue-500 px-6 rounded-full font-bold')

def copy_to_clipboard():
    current_token = token_label.text
    if current_token and current_token != 'Waiting...':
        ui.run_javascript(f'navigator.clipboard.writeText("{current_token}")')
        ui.notify('Token copied to clipboard!', color='green', position='top')
    else:
        ui.notify('No token to copy!', color='red')

with ui.row().classes('w-full justify-between items-center mt-6'):
    time_label = ui.label('Last Update: --:--:--').classes('text-slate-500 text-sm italic')
    
    with ui.row().classes('gap-2'):
        ui.button('COPY', on_click=copy_to_clipboard).classes('bg-emerald-600 hover:bg-emerald-500 font-bold')
        ui.button('REFRESH', on_click=refresh_data).classes('bg-blue-600 hover:bg-blue-500 font-bold')

ui.timer(2.0, refresh_data)

ui.run(title="Entropy Shield", port=8080)