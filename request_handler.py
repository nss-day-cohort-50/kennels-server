from http.server import BaseHTTPRequestHandler, HTTPServer
from animals import get_all_animals, get_tacos, get_single_animal


class HandleRequests(BaseHTTPRequestHandler):
    def _set_headers(self, status):
        self.send_response(status)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        

    def parse_url(self, path):
        path_params = path.split('/')
        resource = path_params[1]
        id = None

        try:
            id = int(path_params[2])
        except IndexError:
            print("they didn't pass in a int")
        except ValueError:
            pass
        return (resource, id)

    def do_OPTIONS(self):
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods',
                         'GET, POST, PUT, DELETE')
        self.send_header('Access-Control-Allow-Headers',
                         'X-Requested-With, Content-Type, Accept')
        self.end_headers()

    def do_GET(self):
        self._set_headers(200)
        # let response;
        response = {}
        # const [posts, setPosts] = useState([])
        (resource, id) = self.parse_url(self.path)
        if resource == "animals":
            if id is not None:
                response = f'{get_single_animal(id)}'
            else:
                response = f'{get_all_animals()}'

        self.wfile.write(response.encode())

    def do_POST(self):
        self._set_headers(201)
        content_len = int(self.headers.get('content-length', 0))
        post_body = self.rfile.read(content_len)
        response = f"received post request: {post_body}"
        self.wfile.write(response.encode())

    def do_PUT(self):
        self.do_POST()


def main():
    host = ''
    port = 8088
    HTTPServer((host, port), HandleRequests).serve_forever()


if __name__ == "__main__":
    main()
