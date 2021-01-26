def jwt_response_payload_handler(token, user=None, request=None):
    """
    自定义jwt认证成功返回数据
    """
    return {
        'user_id': user.id,
        'is_teacher': user.is_staff,
        'username': user.username,
        'token': token,
    }


from django.contrib.auth.backends import ModelBackend
from .models import User
from django.db.models import Q


def get_user_by_other_info(account):
    """
    根据不同的账号类型来获取用户
    :param username:  用户信息，可以是用户名，也可以是邮箱或者手机号码
    :return:
    """
    try:
        user = User.objects.get(Q(username=account) | Q(mobile=account))
        # if user and user.is_staff:
        #     user = User.objects.get(Q(username=account) | Q(mobile=account) | Q(s_id=account))
        #
    except User.DoesNotExist:
        user = None
    return user

class UserInfoModelBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        """
        重写authentication, 以支持多条件登录
        :param request:
        :param username: 用户名或者手机号码或者用户邮箱
        :param password:  登录密码
        :param kwargs:
        :return: 认证后的用户对象
        """

        user = get_user_by_other_info(username)

        if isinstance(user, User) and user.check_password(password) and self.user_can_authenticate(user):
            return user