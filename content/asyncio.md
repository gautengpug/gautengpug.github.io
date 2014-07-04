Title: Introduction to asyncio
Date: 2014-06-29 12:18
Category: Blog
Tags: 2014, asyncio
Author: Frank Millman
Summary: An introductory writeup about Python 3.4's new `asyncio` module.

Introduction to `asyncio`
=========================

> -- <cite>Frank Millman</cite>

If you are writing a server program to handle multiple concurrent connections,
how do you allow the connections to be handled simultaneously without blocking?
There are two main approaches.

The traditional approach uses threads. The main thread runs an endless loop
listening for incoming connections. For each connection received, it creates a
separate thread to handle the connection, and resumes listening. The secondary
thread reads data from the socket and handles it as required, until one side or
the other closes the connection. It runs independently of any other thread, so
it does not have to worry about blocking. It works, but it has two main
disadvantages. Firstly, the operating system limits the number of threads
allowed, so it limits the number of concurrent connections achievable.
Secondly, the operating system switches control between threads arbitrarily,
and the programmer has no control over this. This can lead to subtle bugs,
especially if any state is shared between the threads. This can be managed with
the use of locks and other mechanisms, but if you get it wrong it can be very
hard to debug.

An alternative approach is to use asynchronous I/O. The most popular one in
Python has for some years been a 3rd-party package called
[Twisted](https://twistedmatrix.com/). It also uses an endless loop to listen
for incoming connections, but when one is received it passes control directly
to a request handler within the main thread. The handler reads the data from
the socket, and then handles it up to a point where it might block. At that
point it must do three things. It must define some condition indicating what it
is waiting, it must specify a function to be called when that condition is
satisfied, and it must return, which passes control back to the main loop. In
addition to listening for incoming connections, the main loop also checks all
outstanding conditions. If it finds one that is satisfied, it calls the
specified function so that the handler can continue with its processing. It
sounds complicated, but in practice the majority of current connections are in
a blocked state, so it can handle many connections simultaneously without a
problem. This approach has two main advantages. Firstly, there is no physical
limit to the number of concurrent connections allowed, and many thousands have
been successfully achieved.  Secondly, it is up to each handler to decide when
to relinquish control, so it is easier for handlers to share data safely
without the need for locks.  However, there is a disadvantage - if a handler
does not relinquish control when it is supposed to, the result is that the main
loop cannot continue, and the entire program will appear to have frozen.
Handling this correctly is a skill that comes with experience.


Python has now introduced its own asynchronous I/O capability. It is called
[asyncio](https://docs.python.org/3.4/library/asyncio.html), and it is included
in release 3.4. It is similar to the Twisted approach described above, but
there are some important differences. To explain them, a bit of history is
required.


The `yield` statement was introduced in Python 2.2. Assume a function that
returns more than one result -

    def fetch_rows(first, last):
        rows = []
        for row_no in range(first, last):
            row = fetch_row(row_no)
            rows.append(row)
        return rows

The caller would do something like -

    rows = fetch_rows(first, last)
    for row in rows:
        # do something

This works, but the caller has to wait until all rows are retrieved before
continuing. In the first line, `fetch_rows()` returns a list, and the second
line iterates over the list.

The `yield` statement allows the following -

    def fetch_rows(first, last):
        for row_no in range(first, last):
            row = fetch_row(row_no)
            yield row

The caller looks the same as before, but the sequence of events is different.
The `yield` statement turns the function into a generator. In the first line,
`fetch_rows()` returns a *generator object*. No lines in `fetch_rows()` are
executed yet. The second line iterates over the generator. For the first
iteration, `fetch_rows()` is executed from the first line up to the first
`yield` statement. The value is returned to the caller, but `fetch_rows()`
stays open.  Each subsequent iteration causes `fetch_rows()` to continue from
the line after the `yield` until the next `yield`, or until the function
reaches the end, in which case it raises `StopIteration`. The benefit is that
the caller can process each row as it is retrieved, instead of waiting for them
all to be retrieved.  It also avoids the need to create a list in memory.

The `yield from` statement was introduced in Python 3.3. I cheated here - the
following description is taken directly from the Python
[manual](https://docs.python.org/3/whatsnew/3.3.html#pep-380).

> The `yield from` expression allows a generator to delegate part of its
> operations to another generator. This allows a section of code containing yield
> to be factored out and placed in another generator. Additionally, the
> subgenerator is allowed to return with a value, and the value is made available
> to the delegating generator.
>
> *[...]*
>
> For simple iterators, `yield from iterable` is essentially just a shortened
> form of `for item in iterable: yield item`. *[...]* However, unlike an
> ordinary loop, `yield from` allows subgenerators to receive sent and thrown
> values directly from the calling scope, and return a final value to the outer
> generator.

If you want to learn more, you can read the following -

* [PEP 255](http://legacy.python.org/dev/peps/pep-0255/) - Simple Generators
> The proposal for adding generators and the `yield` statement to Python.

* [PEP 342](http://legacy.python.org/dev/peps/pep-0342/) - Coroutines via
  Enhanced Generators
> The proposal to enhance the API and syntax of generators, making them usable
> as simple coroutines.

* [PEP 380](http://legacy.python.org/dev/peps/pep-0380/) - Syntax for
  Delegating to a Subgenerator
> The proposal to introduce the `yield_from` syntax, making delegation to
> sub-generators easy.


The `asyncio` module was introduced in Python 3.4. From the
[manual](https://docs.python.org/3.4/library/asyncio.html), it 
> provides infrastructure for writing single-threaded concurrent code using
> coroutines, multiplexing I/O access over sockets and other resources, running
> network clients and servers, and other related primitives.

The big difference between Twisted and `asyncio` is that the latter makes
extensive use of the `yield from` statement. In Twisted you have to specify a
callback function to be called when the condition is satisfied, and then
return. With `asyncio` you can use callbacks in the same way, but it is easier
to just call `yield from`, and your function is automatically suspended. When
the condition is satisfied it continues from the next statement. This makes
programs much easier to read and to write.

Here is a simple example of an echo server -

    import asyncio

    def accept_client(client_reader, client_writer):
        task = asyncio.Task(
            handle_client(client_reader, client_writer))

    @asyncio.coroutine
    def handle_client(client_reader, client_writer):
        while True:
            data = yield from asyncio.wait_for(
                client_reader.readline(), timeout=10.0)
            client_writer.write(data))
            if data.decode().rstrip() == 'BYE':
                break

    loop = asyncio.get_event_loop()
    server = asyncio.start_server(accept_client, host, port)
    loop.run_until_complete(server)
    loop.run_forever()

For a fuller example, look at [Python AsyncIO - Streams - Client and
Server](http://davebehnke.com/python-asyncio-streams-client-server.html).

I have only scratched the surface, but I have got it working in my project.
There is a bit of a learning curve to get your head around the concepts, but
most of it *just works*. The problem I found is that if something does not
work, it can be tricky to reason out what is happening. Here is one gotcha that
caught me.

Some of my request handlers are quite complex, so I have refactored them by
splitting them up into smaller functions. If a function needed to block, I
added a `yield from` statement, but then I found that the handler returned
prematurely without doing anything. After much investigation, I found that
adding `yield from` changes the function into a generator (or more strictly, a
coroutine). As explained above, calling a generator simply returns a generator
object, but it does not execute anything. So I tried using `yield from` in the
caller, but this changed *it* into a coroutine, so I found I had to change
every function in the chain into a coroutine by adding the `@asyncio.coroutine`
decorator you can see above to each function, and then invoke it by using
`yield from`. Then everything worked.
