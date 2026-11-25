import project

def main():
    try:
        window = project.MainWindow()
        window.show()
        project.app.exec()
    except Exception as error:
        print(error)

if __name__ == "__main__":
    main()