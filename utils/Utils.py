import threading


def setInterval(func, time, args):
  print(111)
  e = threading.Event()
  while not e.wait(time):
    func(args)
