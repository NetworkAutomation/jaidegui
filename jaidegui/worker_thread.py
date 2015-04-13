#!/usr/bin/env python
""" WorkerThread Class.

Purpose: This class takes command and a queue during construction, runs the
command with the run_jaide() function, in a mp pool for each ip. Any output is
written to the jaidegui.gui.outputArea and potentially also to an output file,
if the user specified so. It also provides functionality for ending the
subprocess before completion.

The class inherits the class threading.Thread, with the purpose of overwriting
the run() method of the standard Thread class.

This Class is part of the jaidegui project.
It is free software for use in manipulating junos devices. More information can
be found at the github page here:

    https://github.com/NetworkAutomation/jaidegui
"""

import threading
import Queue
import multiprocessing
from jaide import wrap
from jaide.color_utils import strip_color
from jaide.utils import clean_lines
from os import path


class WorkerThread(threading.Thread):

    """ WorkerThread class. Used to execute the script in a thread. """

    def __init__(self, argsToPass, sess_timeout, conn_timeout, port, command,
                 stdout, ip, username, password, write_to_file,
                 wtf_style):
        """ Initialize the WorkerThread object.

        Purpose: The initialize function for the WorkerThread Class. The
               | parameters are all used to pass information down to
               | run_jaide() or executing the script properly. Only the ip,
               | wtf_style, and write_to_file parameters are tested against or
               | used within WorkerThread. The rest are simply passed along to
               | run_jaide().

        @param argsToPass: The list of all the arguments that need to be passed
                         | through run_jaide() for proper script execution.
        @type argsToPass: list
        @param sess_timeout: The session timeout value in seconds for the
                           | Jaide object session.
        @type sess_timeout: int
        @param conn_timeout: the connection timeout to use when initally
                       | connecting to the device.
        @type conn_timeout: int
        @param port: the port number on which to connect to the device.
        @type port: int
        @param command: The name of the function within jaide.core.py that we
                      | will be executing to accomplish the goal of the user.
                      | An example of this being deciphered and used is within
                      | the class jaidegui.gui.__init__() method.
        @type command: function
        @param stdout: A queue where all output will be put, the
                     | write_to_queue() method is used as a callback
                     | function for the run_jaide() method, so that any
                     | results from run_jaide() are written to
                     | stdout. stdout is actively watched
                     | by the jaidegui.gui.__getoutput() method for printing
                     | output to the user.
        @type stdout: Queue.Queue()
        @param ip: The IP string can be one of three things: A single IP
                 | address, a comma separated list of IPs, or a filepath
                 | pointing to a plaintext file of IPs, each one on a separate
                 | line.
        @type ip: str
        @param username: The username for authenticating against the device(s)
        @type username: str
        @param password: The password for authenticating against the device(s)
        @type password: str
        @param write_to_file: Either an empty string (meaning we're not writing
                            | to a file), or a filepath pointing to the desired
                            | output file for the script output.
                            | jaidegui.gui.run() will determine if we're
                            | writing to a file or not and passes in the
                            | appropriate value.
        @type write_to_file: str
        @param wtf_style: How to dump the output, either to a single file or to
                        | multiple, one for each host. Possible values are:
                        | ['s', 'single', 'm', 'multiple']
        @type wtf_style: str

        @returns: None
        """
        super(WorkerThread, self).__init__()
        self.argsToPass = argsToPass
        self.sess_timeout = sess_timeout
        self.command = command
        self.stdout = stdout
        self.ip = ip
        self.port = port
        self.conn_timeout = conn_timeout
        self.username = username
        self.password = password
        self.write_to_file = write_to_file
        # Set number of threads to 2x number of cores. Usually cpu_count
        # returns twice the physical cores due to hyperthreading.
        self.mp_pool = multiprocessing.Pool(multiprocessing.cpu_count() * 2)
        self.wtfQueue = Queue.Queue()
        self.wtf_style = wtf_style

    def write_to_queue(self, results):
        """ Write script output to the queue.

        Purpose: This function is used for callback from pressing the 'Run
               | Script' button. It will always output to the stdout,
               | which __writeToOutputArea is watching, and will therefore
               | be showed to the user within the output area at the bottom
               | of the application.
               |
               | The if statement will also put the outputs into the queue
               | being watched by the 'run' function, which will output the
               | results to the output file they specified.

        @param results: the results that will be dropped into the output area,
                      | and possibly also the output file, if write_to_file is
                      | true/checked.
        @type results: tuple, with the output string in index 1

        @returns: None
        """
        # jaide.wrap.open_connection returns a tuple, with the second index
        # being the output, but we strip the ANSI color codes.
        results = strip_color(results[1])
        self.stdout.put(results)
        if self.write_to_file:
            self.wtfQueue.put(results)

    def run(self):
        """ Overwrite threading.Thread run method.

        Purpose: This overwrites threading.Thread's run() method. It is called
               | by doing WorkerThread.start(). The overaching goal is to
               | open a multiprocessing pool and execute the run_jaide()
               | function against each IP supplied to us.
               |
               | We callback to write_to_queue() for a list of IP addresses.
               | Once we have executed the script, we check the write_to_file
               | parameter to see if we need to output to a file.

        @returns: None
        """
        # build the list of IPs
        iplist = [ip for ip in clean_lines(self.ip)]
        for ip in iplist:
            # TODO: set back to mp_pool before finishing release. This is only set as is to receive errors.
            # self.write_to_queue(run_jaide(ip.strip(), self.username,
            #                               self.password, self.command,
            #                               self.sess_timeout, self.argsToPass,
            #                               self.conn_timeout, self.port))
            self.mp_pool.apply_async(run_jaide, args=(ip.strip(),
                                                      self.username,
                                                      self.password,
                                                      self.command,
                                                      self.sess_timeout,
                                                      self.argsToPass,
                                                      self.conn_timeout,
                                                      self.port),
                                     callback=self.write_to_queue)
        self.mp_pool.close()
        self.mp_pool.join()

        if self.write_to_file:
            # Just dumping all output to a single file.
            if self.wtf_style in ["s", "single"]:
                try:
                    out_file = open(self.write_to_file, "a+b")
                except IOError as e:
                    self.stdout.put("Could not save script output to file."
                                    " Error:\n" + str(e))
                else:
                    while not self.wtfQueue.empty():
                        out_file.write(self.wtfQueue.get())
                    self.stdout.put("\nSuccessfully appended output to: "
                                    "%s\n" % self.write_to_file)
            # Dump output to one file for each IP touched.
            elif self.wtf_style in ["m", 'multiple']:
                temp_output = ""
                while not self.wtfQueue.empty():
                    temp_output += self.wtfQueue.get()
                temp_output = temp_output.split("=" * 50)
                for x in range(1, len(temp_output)):
                    # get each of the IP/hostnames we touched
                    ip = temp_output[x].split('Results from device: ')[1].split('\n')[0].strip()
                    # inject the ip into the front of the filename
                    filepath = path.join(path.split(self.write_to_file)[0],
                                         ip + "_" +
                                         path.split(self.write_to_file)[1])
                    try:
                        out_file = open(filepath, 'a+b')
                    # use stdout.put here instead of write_to_queue since it is
                    # not usable after we've already written everything
                    # to the file.
                    except IOError as e:
                        self.stdout.put('Error opening output file \'%s\' for'
                                        ' writing. The Error was:\n%s' %
                                        (filepath, str(e)))
                    else:
                        out_file.write(temp_output[x])
                        self.stdout.put('\nOutput written/appended to: ' +
                                        filepath)
                        out_file.close()

    def join(self, timeout=None):
        """ Join the multiprocessing pool.

        Purpose: Provide a method for joining the threads to the main-thread,
               | to ensure that the parent thread (jgui) knows when the
               | sub-thread (WorkerThread) has finished, and can continue.

        @param timeout: the integer value used for the timeout joining the
                      | thread.
        @type timeout: int

        @returns: None
        """
        super(WorkerThread, self).join(timeout)

    def kill_proc(self):
        """ Terminate the multiprocessing pool.

        Purpose: Provide a way to kill the subprocess from outside of the
               | thread. Terminating the pool leaves nothing left blocking
               | self.run() so it completes and exits normally.

        @returns: None
        """
        self.mp_pool.terminate()


def run_jaide(ip, username, password, function, sess_timeout, argsToPass,
              conn_timeout, port):
    """ Run the jaide_cli script to retrieve the device output.

    Purpose: This function is created outside of the WorkerThread class due
           | to the limitation that a method within the WorkerThread
           | class could not be 'pickled' for multiprocessing when running
           | against more than one IP address.

    @param ip: The ip address, comma separated list of ip addresses, or the
             | filepath of the file containing the ip addresses.
    @type ip: str
    @param username: The username for authenticating against the device.
    @type username: str
    @param password: The password for authenticating against the device.
    @type password: str
    @param function: The name of the function within jaide_tool.py that we
                  | will be executing to accomplish the goal of the user.
                  | An example of this being deciphered and used is within
                  | the class jaidegui.gui.__init__() method.
    @type function: function
    @param sess_timeout: The session timeout value in seconds for the
                       | Jaide object session.
    @type sess_timeout: int
    @param argsToPass: The list of all the arguments that need to be passed
                     | through run_jaide() to jaide_tool.open_connection().
    @type argsToPass: list
    @param conn_timeout: the connection timeout to use when initally
                       | connecting to the device.
    @type conn_timeout: int
    @param port: the port number on which to connect to the device.
    @type port: int

    @returns: the output from the jaide command. It will have ANSI color
            | in the string. These are stripped out later.
    @rtype: str
    """
    return wrap.open_connection(ip, username, password, function,
                                argsToPass, "", conn_timeout,
                                sess_timeout, port)
