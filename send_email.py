import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(sender_email, sender_password, receiver_email, subject, body):
    """
    发送邮件函数

    参数:
    sender_email: 发送方邮箱地址
    sender_password: 发送方邮箱授权码或应用专用密码
    receiver_email: 收件人邮箱地址
    subject: 邮件主题
    body: 邮件正文
    """
    # 创建 MIME 消息对象
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # 将邮件正文内容附加到邮件消息中
    msg.attach(MIMEText(body, 'plain'))

    # 配置 163 的 SMTP 服务器
    smtp_server = "smtp.163.com"
    smtp_port = 465  # 465 端口支持 SSL 加密

    # 连接到 SMTP 服务器并发送邮件
    server = None
    try:
        # 使用 SSL 连接 SMTP 服务器
        server = smtplib.SMTP_SSL(smtp_server, smtp_port)
        # 登录邮箱
        server.login(sender_email, sender_password)
        # 将 MIME 消息转换为字符串
        text = msg.as_string()
        # 发送邮件
        server.sendmail(sender_email, receiver_email, text)
        print("邮件发送成功！")
    except Exception as e:
        print(f"邮件发送失败: {e}")
    finally:
        if server:
            server.quit()  # 确保在 server 被成功创建后才调用 quit()
        else:
            print('SMTP 连接失败')

def main():
    """
    主函数，定义邮件发送的相关信息并调用发送邮件函数
    """
    sender_email = "crescent202412@163.com"  # 发送邮件的邮箱地址
    sender_password = "BAa5wRd5z7A6Jc7M"  # 授权码或应用专用密码
    receiver_email = "3319535521@qq.com"  # 收件人的邮箱地址
    subject = "测试邮件"  # 邮件主题
    body = "这是一封测试邮件，使用 Python 从 163 邮箱发送！"  # 邮件正文内容

    # 调用 send_email 函数发送邮件
    send_email(sender_email, sender_password, receiver_email, subject, body)

if __name__ == "__main__":
    main()
