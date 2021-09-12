"""we are going to implement an HTTPRouter like you would find in a typical web server 
using the Trie data structure

There are many different implementations of HTTP Routers 
    such as regular expressions or simple string matching,
    but the Trie is an excellent and very efficient data structure for this purpose

The purpose of an HTTP Router is to 
    take a URL path like "/", "/about", or "/blog/2019-01-15/my-awesome-blog-post"
    and figure out what content to return. 
    In a dynamic web server, the content will often come from a block of code called a handler.

Instead of simple words the Trie will contain a part of the http path at each node, 
building from the root node "/"

We just need to insert and find nodes, 
and if a RouteTrieNode is not a leaf node, it won't have a handler

A sensible way to split things would be on the parts of the path that are separated by slashes ("/"). 
A Trie with a single path entry of: "/about/me" would look like:
(root, None) -> ("about", None) -> ("me", "About Me handler")

The router will initialize itself with a RouteTrie for holding routes and associated handlers. 
It should also support adding a handler by path and looking up a handler by path. 
All of these operations will be delegated to the RouteTrie.
"""

# A RouteTrieNode will be similar to our autocomplete TrieNode... with one additional element, a handler.
from typing import List


class RouteTrieNode:
    def __init__(self, handler=None):
        self.children = {}
        self.handler = handler

    def insert(self, part):
        if part not in self.children:
            self.children[part] = RouteTrieNode()


# A RouteTrie will store our routes and their associated handlers
class RouteTrie:
    def __init__(self, handler: str):
        self.root = RouteTrieNode(handler)
        self.handler = handler  # doing self.root.handler would result in something like router.router.root.handler

    def insert(self, path: List[str], handler: str):
        node = self.root

        for part in path:
            node.insert(part)
            node = node.children[part]

        node.handler = handler

    def find(self, path: List[str]):
        node = self.root

        for part in path:
            if part not in node.children:
                return None
            node = node.children[part]
        return node.handler


class Router:
    def __init__(self, handler: str):
        self.router = RouteTrie(handler)
        self.handler_not_found = "404: handler not found"

    def add_handler(self, raw_path, handler):
        """split the path and pass parts as a list to the RouteTrie"""
        _path_parts = self.parse_path(raw_path)
        self.router.insert(_path_parts, handler)

    def lookup(self, raw_path):
        """lookup path (by parts) and return the associated handler"""
        path = self.parse_path(raw_path)

        if len(path) == 0:
            return self.router.handler
            
        _result = self.router.find(path)

        return self.handler_not_found if _result is None else _result


    @staticmethod
    def parse_path(raw: str) -> List[str]:
        """split the path into parts for both the add_handler and loopup functions"""
        return [part for part in raw.strip().split("/")]


router = Router("root handler")
router.add_handler("/home/about", "about handler")  # add a route


assert router.lookup("/") == "root handler"
assert(router.lookup("/home") == "not found handler")
assert(router.lookup("/home/about") == "about handler")
assert(router.lookup("/home/about/") == "about handler")
assert(router.lookup("/home/about/me") == "not found handler")
