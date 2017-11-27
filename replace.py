import argparse


_S = """uid_4\""""
_R = """uid_4\" elementtiming\=\"hero\""""


class Replacer:
    def response(self, flow):
        flow.response.replace(_S, _R)


def start():
    parser = argparse.ArgumentParser()
    args = parser.parse_args()
    return Replacer()
