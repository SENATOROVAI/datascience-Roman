# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.16.4
#   kernelspec:
#     display_name: base
#     language: python
#     name: python3
# ---

"""Module for git."""

# +
git pull - принять апдейт, всегда делать перед коммитом

# эти комманлы обычно вводятся автоматически
git add . - добавляем все файлы в трекинг
git commit -m "commit title"
git push
# -

# нажимаем Sync fork, Если репозиторий организации обновился и опережает по коммитам, процедура называется "ПОдтянуть ветку"
# ![image.png](attachment:image.png)

# отправляем pull request, если хотим помочь проекту
# ![image.png](attachment:image.png)

# 27.10.24
#
# 1. распаковали последний релиз v.1.0.3 в репозиторий
# 2. обновили файлы в репозитории, команды 
# # go to the folder
# # cd pre-commit 
#
# # update release
# git pull
# 3. форкнули репозиторий pre-commit
# 4. завели issues
# 5. сделали pull request
