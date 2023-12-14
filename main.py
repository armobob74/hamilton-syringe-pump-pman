from website import create_app

app = create_app()

if __name__ == '__main__':
    import sys
     # Check if a port number is provided
    if len(sys.argv) > 1:
        try:
            port = int(sys.argv[1])
        except ValueError:
            port = 5010
            print(f"No valid port provided. Using default port {port}.")
    else:
        port = 5010
    app.config['HOST_PORT'] = port
    app.run(debug=True, port=port)
