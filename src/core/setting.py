from typing import TypedDict
from validkit import v, validate

class ServerSetting(TypedDict):
    """
    サーバーごとの設定
    """
    id: int

class GuildUserSetting(TypedDict):
    """
    サーバーごとのユーザー設定
    """
    id: int
    guild_id: int

def migrate_setting(setting: dict, migrate: dict) -> ServerSetting:
    """
    自動で古いバージョンの設定データを自動的に新しい形式へ変換します。
    :param setting:
    :param migrate:
    :return:
    """
    migrated = validate(
        setting,
        ServerSetting,
        migrate=migrate,
    )
    return migrated

def validate_setting(setting: dict) -> ServerSetting:
    """
    サーバー設定の整合性を検証します。
    :param setting:
    :return:
    """
    return validate(setting, ServerSetting)

def validate_guild_user_setting(setting: dict) -> GuildUserSetting:
    """
    サーバーごとのユーザー設定を検証します。
    :param setting:
    :return:
    """
    return validate(setting, GuildUserSetting)