import time
import vk_api
import requests

VK_TOKEN = ''
# Получить можно на https://vkhost.github.io/ - советую "Вк звонки" как приложение ставить


VK_USER_ID = '123456789'
DISCORD_WEBHOOK_URL = 'https://discord.com/api/webhooks/1234234563457634567/xxxxxxxxxxxxxxxxxxxx'


def check_vk_online(vk_session, user_id):
    try:
        vk = vk_session.get_api()
        user_info = vk.users.get(user_ids=user_id, fields='online')[0]
        return user_info['online']
    except Exception as e:
        print("Ошибка при проверке статуса ВКонтакте:", e)
        return False


def send_discord_message(webhook_url, message):
    try:
        payload = {'content': message}
        response = requests.post(webhook_url, json=payload)
        if response.status_code == 204:
            print("Сообщение успешно отправлено в Discord")
        else:
            print("Не удалось отправить сообщение в Discord. Код ответа:", response.status_code)
    except Exception as e:
        print("Ошибка при отправке сообщения в Discord:", e)


def main():
    vk_session = vk_api.VkApi(token=VK_TOKEN)

    while True:
        try:
            online = check_vk_online(vk_session, VK_USER_ID)
            if online:
                send_discord_message(DISCORD_WEBHOOK_URL, f"Пользователь с ID {VK_USER_ID} в сети!")
            else:
                print("Пользователь в офлайне")
        except Exception as e:
            print("Ошибка:", e)
        time.sleep(60)


if __name__ == "__main__":
    main()
