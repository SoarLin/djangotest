#!/bin/bash
echo "安裝虛擬運行環境"
python3 -m venv VENV

echo "切換到虛擬環境下"
source VENV/bin/activate

# echo "建立專案資料夾"
# django-admin.py startproject mysite

echo "運行 Django"
echo "指令 python manage.py runserver"