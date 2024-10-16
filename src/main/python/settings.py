import yaml

class Settings:
    def __init__(self, base_url, auth_env_var, epic_jql, epic_due_date_field, epic_start_date_field, story_point_field, story_done_status):
        self.base_url = base_url
        self.auth_env_var = auth_env_var
        self.epic_jql = epic_jql
        self.epic_due_date_field = epic_due_date_field
        self.epic_start_date_field = epic_start_date_field
        self.story_point_field = story_point_field
        self.story_done_status = story_done_status

    def __repr__(self):
        return (f"Settings(base_url={self.base_url}, auth_env_var={self.auth_env_var}, "
                f"epic_jql={self.epic_jql}, epic_due_date_field={self.epic_due_date_field}, "
                f"epic_start_date_field={self.epic_start_date_field}, story_point_field={self.story_point_field}, "
                f"story_done_status={self.story_done_status})")

def load_settings_from_yaml(file_path):
    with open(file_path, 'r') as file:
        data = yaml.safe_load(file)
        settings = Settings(
            base_url=data['base_url'],
            auth_env_var=data['auth_env_var'],
            epic_jql=data['epic_jql'],
            epic_due_date_field=data['epic_due_date_field'],
            epic_start_date_field=data['epic_start_date_field'],
            story_point_field=data['story_point_field'],
            story_done_status=data['story_done_status']
        )
        return settings

