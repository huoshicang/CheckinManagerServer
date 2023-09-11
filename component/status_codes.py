HTTP_STATUS_CODES = {
    'OK': 200,  # 请求成功
    'CREATED': 201,  # 已创建（通常在创建资源时使用）
    'BAD_REQUEST': 400,  # 请求无效或不完整
    'UNAUTHORIZED': 401,  # 未经授权，需要提供身份验证凭据
    'FORBIDDEN': 403,  # 禁止访问，客户端没有权限
    'NOT_FOUND': 404,  # 请求的资源不存在
    'INTERNAL_SERVER_ERROR': 500,  # 服务器内部错误
}


def BAD_REQUEST():
    """
    缺少必要的参数 400
    """
    return {
        "code": HTTP_STATUS_CODES['BAD_REQUEST'],
        "data": [],
        "message": "缺少必要的参数"
    }


def BAD_REQUEST2():
    """
    缺少必要的参数 400
    """
    return {
        "code": HTTP_STATUS_CODES['BAD_REQUEST'],
        "data": [],
        "message": "请求无效"
    }

def INTERNAL_SERVER_ERROR():
    """
    服务器内部错误 500
    """
    return {
        "code": HTTP_STATUS_CODES['INTERNAL_SERVER_ERROR'],
        "data": [],
        "message": "服务器内部错误"
    }


def NOT_FOUND():
    """
    没有信息 404
    """
    return {
        "code": HTTP_STATUS_CODES['NOT_FOUND'],  # 使用 HTTP 404 表示未找到
        "data": [],
        "message": "没有信息"
    }
