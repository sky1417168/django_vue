# 启动前端开发服务器
Start-Process -NoNewWindow -FilePath "cmd.exe" -ArgumentList "/k cd frontend && npm run serve"

# 启动后端 Django 服务器
Start-Process -NoNewWindow -FilePath "cmd.exe" -ArgumentList "/k cd backend && python manage.py runserver"
