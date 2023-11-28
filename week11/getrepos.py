from github import Github
import json

# 使用您的 GitHub 令牌
g = Github("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")

# 获取当前用户
user = g.get_user()

# 创建一个空字典来存储您关注的用户及其仓库信息
following_repos = {}

# 获取并遍历您关注的用户
for following in user.get_following():
    # 获取每个用户的仓库
    repos = following.get_repos()
    # 将仓库名称添加到字典
    following_repos[following.login] = [repo.name for repo in repos]

# 将数据保存为 JSON 文件
with open("following_repos.json", "w") as file:
    json.dump(following_repos, file)

print("完成，您关注的用户的仓库信息已保存到 'following_repos.json'")
