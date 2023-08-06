if __name__ == "__main__":
    # from documentationAI.interfaces.cli import main
    # main()
    # DIコンテナで解決されたclass CLIインスタンスを取得して，cli.run()を実行する
    from documentationAI.container import container
    cli = container.cli()
    cli.run()
