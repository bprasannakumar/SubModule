from MainModule.app.main_cron import execute_main_cron


def execute_submod_cron():
    print("execute_submod_cron from submod_cron.py")
    execute_main_cron()


if __name__ == "__main__":
    execute_submod_cron()
