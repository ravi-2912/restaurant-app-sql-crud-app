#!/usr/bin/env python3

# import nodules for server application
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import restaurant_crud as CRUD
import os

# basic HTML template
html = '''
<!DOCTYPE html>
    <title>Restauant App</title>
    <body/>
        {data}
    </body>
</html>
'''


class MyHandler(BaseHTTPRequestHandler):
    """Class to handle GET and POST requests"""

    def do_GET(self):
        try:
            path = self.path
            self.send_response(200)
            self.send_header("content-type", "text/html; charset=utf-8")
            self.end_headers()
            if path.endswith("/"):
                data = "<h1>Restaurant App</h1>"
                data += "<h3>Restaurants List</h1>"
                for r in CRUD.get_restaurants():
                    data += '''<p>
                                {name}<br>
                                <a href="/restaurant/{id}/edit">Edit</a>
                                <a href="/restaurant/{id}/delete">Delete</a>
                            </p>'''.format(name=r.name, id=r.id)
                data += '''<h3>Add a new restaurant</h3>
                        <form method="POST">
                            <input type="text" name="name" placeholder="Type name...">
                            <button type="submit" value="INSERT">Add</button>
                        </form>'''
            elif path.endswith("/delete"):
                r_id = int(path.split("/")[2])
                r = CRUD.get_restaurant(r_id)
                data = "<h2>Are you sure you want to delete: {}?</h2>".format(r.name)
                data += '''<form method="POST">
                            <button type="submit" value="delete" name="action">Delete</button>
                            <button type="submit" value="cancel" name="action">Cancel</button>
                        </form>'''
            elif path.endswith("/edit"):
                r_id = int(path.split("/")[2])
                r = CRUD.get_restaurant(r_id)
                data = "<h2>Are you sure you want to rename: {}?</h2>".format(r.name)
                data += '''<form method="POST">
                            <input type="text" name="newName" placeholder="Type name...">
                            <button type="submit" value="update" name="action">Update</button>
                            <button type="submit" value="cancel" name="action">Cancel</button>
                        </form>'''

            self.wfile.write(html.format(data=data).encode())
            return True
        except IOError:
             self.send_error(404, 'File Not Found: %s' % self.path)
             return False

    def do_POST(self):
        try:
            length = int(self.headers.get('Content-length', 0))
            data = self.rfile.read(length).decode()
            path = self.path
            message = parse_qs(data)
            if path.endswith("/"):
                CRUD.create_restaurant(message["name"][0])
            elif path.endswith("/delete"):
                if(message["action"][0] == "delete"):
                    r_id = path.split("/")[2]
                    CRUD.delete_restaurant(r_id)
            elif path.endswith("/edit"):
                print(message)
                if(message["action"][0] == "update"):
                    r_id = path.split("/")[2]
                    CRUD.update_restaurant_name(r_id, message["newName"][0])
            self.send_response(303)
            self.send_header('Location', '/')
            self.end_headers()
            return True
        except:
            return False



# commands to run the server on localhost at port 8000
if __name__ == "__main__":
    try:
        port = int(os.environ.get('PORT', 8000))
        server = HTTPServer(("", port), MyHandler)
        server.serve_forever()
    except KeyboardInterrupt:
        print (" ^C entered, stopping web server....")
        server.socket.close()




