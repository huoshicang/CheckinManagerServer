# 登录 注册 退出
from Api.UserLog.UserLogIn import LogIn
from Api.UserLog.UserLogUp import LogUp
from Api.UserLog.UserLogOut import LogOut

# 系统用户信息
from Api.User.GetUserInfo import GetUserInfo # 获取用户
from Api.User.UpUserInfo import UpInfo # 更新签到信息标识
from Api.User.DelUserInfo import DelUserInfo # 删除用户
from Api.User.ModifyUserInfo import Modify # 编辑用户
from Api.User.ResetPassword import ResetPassword # 重置密码
from Api.User.ChangePassword import ChangePassword # 修改密码

# 签到用户信息
from Api.CheckIn.GetCheckInfo import GetCheckInfo
from Api.CheckIn.AddCheckInfo import AddCheckInfo
from Api.CheckIn.ModifyCheckInfo import Modify
from Api.CheckIn.DelCheckInfo import DelCheck

# 周报
from Api.Weekly.GetWeeklyData import GetWeekly
from Api.Weekly.DelWeeklyData import DelWeekly
from Api.Weekly.AddWeeklyData import AddWeekly
from Api.Weekly.ModifyWeeklyData import ModifyWeekly

# 月报
from Api.Month.GetMonthData import GetMonth
from Api.Month.DelMonthData import DelMonth
from Api.Month.AddMonthData import AddMonth
from Api.Month.ModifyMonthData import ModifyMonth

# 任务
from Api.Quest.GetCheckQuest import GetCheckQuest
# from Api.Quest.DelWeeklyData import DelWeekly
# from Api.Quest.AddWeeklyData import AddWeekly
# from Api.Quest.ModifyWeeklyData import ModifyWeekly
