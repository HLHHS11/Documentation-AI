if __name__ == "__main__":
    import os
    from dotenv import load_dotenv
    from documentationAI.container import container

    load_dotenv(verbose=True)
    dotenv_path = os.path.join(os.path.dirname(__file__), '../', '.env')
    load_dotenv(dotenv_path)

    cli = container.cli()
    cli.run()
