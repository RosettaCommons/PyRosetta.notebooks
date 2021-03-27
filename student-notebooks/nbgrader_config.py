c = get_config()

###############################################################################
# Begin additions by nbgrader quickstart
###############################################################################

# You only need this if you are running nbgrader on a shared
# server set up.
c.CourseDirectory.course_id = "student-notebooks"

# Update this list with other assignments you want
c.CourseDirectory.db_assignments = [dict(name="ps1")]

# Change the students in this list with that actual students in
# your course
c.CourseDirectory.db_students = [
    dict(id="bitdiddle", first_name="Ben", last_name="Bitdiddle"),
    dict(id="hacker", first_name="Alyssa", last_name="Hacker"),
    dict(id="reasoner", first_name="Louis", last_name="Reasoner")
]

c.IncludeHeaderFooter.header = "source/header.ipynb"

###############################################################################
# End additions by nbgrader quickstart
###############################################################################

# Configuration file for nbgrader-generate-config.

#------------------------------------------------------------------------------
# Application(SingletonConfigurable) configuration
#------------------------------------------------------------------------------
## This is an application.

## The date format used by logging formatters for %(asctime)s
#  Default: '%Y-%m-%d %H:%M:%S'
# c.Application.log_datefmt = '%Y-%m-%d %H:%M:%S'

## The Logging format template
#  Default: '[%(name)s]%(highlevel)s %(message)s'
# c.Application.log_format = '[%(name)s]%(highlevel)s %(message)s'

## Set the log level by value or name.
#  Choices: any of [0, 10, 20, 30, 40, 50, 'DEBUG', 'INFO', 'WARN', 'ERROR', 'CRITICAL']
#  Default: 30
# c.Application.log_level = 30

## Instead of starting the Application, dump configuration to stdout
#  Default: False
# c.Application.show_config = False

## Instead of starting the Application, dump configuration to stdout (as JSON)
#  Default: False
# c.Application.show_config_json = False

#------------------------------------------------------------------------------
# JupyterApp(Application) configuration
#------------------------------------------------------------------------------
## Base class for Jupyter applications

## Answer yes to any prompts.
#  Default: False
# c.JupyterApp.answer_yes = False

## Full path of a config file.
#  Default: ''
# c.JupyterApp.config_file = ''

## Specify a config file to load.
#  Default: ''
# c.JupyterApp.config_file_name = ''

## Generate default config file.
#  Default: False
# c.JupyterApp.generate_config = False

## The date format used by logging formatters for %(asctime)s
#  See also: Application.log_datefmt
# c.JupyterApp.log_datefmt = '%Y-%m-%d %H:%M:%S'

## The Logging format template
#  See also: Application.log_format
# c.JupyterApp.log_format = '[%(name)s]%(highlevel)s %(message)s'

## Set the log level by value or name.
#  See also: Application.log_level
# c.JupyterApp.log_level = 30

## Instead of starting the Application, dump configuration to stdout
#  See also: Application.show_config
# c.JupyterApp.show_config = False

## Instead of starting the Application, dump configuration to stdout (as JSON)
#  See also: Application.show_config_json
# c.JupyterApp.show_config_json = False

#------------------------------------------------------------------------------
# NbGrader(JupyterApp) configuration
#------------------------------------------------------------------------------
## A base class for all the nbgrader apps.

## Answer yes to any prompts.
#  See also: JupyterApp.answer_yes
# c.NbGrader.answer_yes = False

## Full path of a config file.
#  See also: JupyterApp.config_file
# c.NbGrader.config_file = ''

## Specify a config file to load.
#  See also: JupyterApp.config_file_name
# c.NbGrader.config_file_name = ''

## Generate default config file.
#  See also: JupyterApp.generate_config
# c.NbGrader.generate_config = False

## The date format used by logging formatters for %(asctime)s
#  See also: Application.log_datefmt
# c.NbGrader.log_datefmt = '%Y-%m-%d %H:%M:%S'

## The Logging format template
#  See also: Application.log_format
# c.NbGrader.log_format = '[%(name)s]%(highlevel)s %(message)s'

## Set the log level by value or name.
#  See also: Application.log_level
# c.NbGrader.log_level = 30

## Name of the logfile to log to. By default, log output is not written to any
#  file.
#  Default: ''
# c.NbGrader.logfile = ''

## Instead of starting the Application, dump configuration to stdout
#  See also: Application.show_config
# c.NbGrader.show_config = False

## Instead of starting the Application, dump configuration to stdout (as JSON)
#  See also: Application.show_config_json
# c.NbGrader.show_config_json = False

#------------------------------------------------------------------------------
# GenerateConfigApp(NbGrader) configuration
#------------------------------------------------------------------------------
## Answer yes to any prompts.
#  See also: JupyterApp.answer_yes
# c.GenerateConfigApp.answer_yes = False

## Full path of a config file.
#  See also: JupyterApp.config_file
# c.GenerateConfigApp.config_file = ''

## Specify a config file to load.
#  See also: JupyterApp.config_file_name
# c.GenerateConfigApp.config_file_name = ''

## The name of the configuration file to generate.
#  Default: 'nbgrader_config.py'
# c.GenerateConfigApp.filename = 'nbgrader_config.py'

## Generate default config file.
#  See also: JupyterApp.generate_config
# c.GenerateConfigApp.generate_config = False

## The date format used by logging formatters for %(asctime)s
#  See also: Application.log_datefmt
# c.GenerateConfigApp.log_datefmt = '%Y-%m-%d %H:%M:%S'

## The Logging format template
#  See also: Application.log_format
# c.GenerateConfigApp.log_format = '[%(name)s]%(highlevel)s %(message)s'

## Set the log level by value or name.
#  See also: Application.log_level
# c.GenerateConfigApp.log_level = 30

## 
#  See also: NbGrader.logfile
# c.GenerateConfigApp.logfile = ''

## Instead of starting the Application, dump configuration to stdout
#  See also: Application.show_config
# c.GenerateConfigApp.show_config = False

## Instead of starting the Application, dump configuration to stdout (as JSON)
#  See also: Application.show_config_json
# c.GenerateConfigApp.show_config_json = False

#------------------------------------------------------------------------------
# CourseDirectory(LoggingConfigurable) configuration
#------------------------------------------------------------------------------
## The assignment name. This MUST be specified, either by setting the config
#  option, passing an argument on the command line, or using the --assignment
#  option on the command line.
#  Default: ''
# c.CourseDirectory.assignment_id = ''

## The name of the directory that contains assignment submissions after they have
#  been autograded. This corresponds to the `nbgrader_step` variable in the
#  `directory_structure` config option.
#  Default: 'autograded'
# c.CourseDirectory.autograded_directory = 'autograded'

## A key that is unique per instructor and course. This can be specified, either
#  by setting the config option, or using the --course option on the command
#  line.
#  Default: ''
# c.CourseDirectory.course_id = ''

## A list of assignments that will be created in the database. Each item in the
#  list should be a dictionary with the following keys:
#  
#      - name
#      - duedate (optional)
#  
#  The values will be stored in the database. Please see the API documentation on
#  the `Assignment` database model for details on these fields.
#  Default: []
# c.CourseDirectory.db_assignments = []

## A list of student that will be created in the database. Each item in the list
#  should be a dictionary with the following keys:
#  
#      - id
#      - first_name (optional)
#      - last_name (optional)
#      - email (optional)
#  
#  The values will be stored in the database. Please see the API documentation on
#  the `Student` database model for details on these fields.
#  Default: []
# c.CourseDirectory.db_students = []

## URL to the database. Defaults to sqlite:///<root>/gradebook.db, where <root>
#  is another configurable variable.
#  Default: ''
# c.CourseDirectory.db_url = ''

## Format string for the directory structure that nbgrader works over during the
#  grading process. This MUST contain named keys for 'nbgrader_step',
#  'student_id', and 'assignment_id'. It SHOULD NOT contain a key for
#  'notebook_id', as this will be automatically joined with the rest of the path.
#  Default: '{nbgrader_step}/{student_id}/{assignment_id}'
# c.CourseDirectory.directory_structure = '{nbgrader_step}/{student_id}/{assignment_id}'

## The name of the directory that contains assignment feedback after grading has
#  been completed. This corresponds to the `nbgrader_step` variable in the
#  `directory_structure` config option.
#  Default: 'feedback'
# c.CourseDirectory.feedback_directory = 'feedback'

## Make all instructor files group writeable (g+ws, default g+r only) and
#  exchange directories group readable/writeable (g+rws, default g=nothing only )
#  by default.  This should only be used if you carefully set the primary groups
#  of your notebook servers and fully understand the unix permission model.  This
#  changes the default permissions from 444 (unwriteable) to 664 (writeable), so
#  that other instructors are able to delete/overwrite files.
#  Default: False
# c.CourseDirectory.groupshared = False

## List of file names or file globs. Upon copying directories recursively,
#  matching files and directories will be ignored with a debug message.
#  Default: ['.ipynb_checkpoints', '*.pyc', '__pycache__', 'feedback']
# c.CourseDirectory.ignore = ['.ipynb_checkpoints', '*.pyc', '__pycache__', 'feedback']

## List of file names or file globs. Upon copying directories recursively, non
#  matching files will be ignored with a debug message.
#  Default: ['*']
# c.CourseDirectory.include = ['*']

## Maximum size of files (in kilobytes; default: 100Mb). Upon copying directories
#  recursively, larger files will be ignored with a warning.
#  Default: 100000
# c.CourseDirectory.max_file_size = 100000

## File glob to match notebook names, excluding the '.ipynb' extension. This can
#  be changed to filter by notebook.
#  Default: '*'
# c.CourseDirectory.notebook_id = '*'

## The name of the directory that contains the version of the assignment that
#  will be released to students. This corresponds to the `nbgrader_step` variable
#  in the `directory_structure` config option.
#  Default: 'release'
# c.CourseDirectory.release_directory = 'release'

## The root directory for the course files (that includes the `source`,
#  `release`, `submitted`, `autograded`, etc. directories). Defaults to the
#  current working directory.
#  Default: ''
# c.CourseDirectory.root = ''

## The name of the directory that contains the master/instructor version of
#  assignments. This corresponds to the `nbgrader_step` variable in the
#  `directory_structure` config option.
#  Default: 'source'
# c.CourseDirectory.source_directory = 'source'

## File glob to match student IDs. This can be changed to filter by student.
#  Note: this is always changed to '.' when running `nbgrader assign`, as the
#  assign step doesn't have any student ID associated with it. With `nbgrader
#  submit`, this instead forces the use of an alternative student ID for the
#  submission. See `nbgrader submit --help`.
#  
#  If the ID is purely numeric and you are passing it as a flag on the command
#  line, you will need to escape the quotes in order to have it detected as a
#  string, for example `--student=""12345""`. See:
#  
#      https://github.com/jupyter/nbgrader/issues/743
#  
#  for more details.
#  Default: '*'
# c.CourseDirectory.student_id = '*'

## Comma-separated list of student IDs to exclude.  Counterpart of student_id.
#  
#  This is useful when running commands on all students, but certain students
#  cause errors or otherwise must be left out.  Works at least for autograde,
#  generate_feedback, and release_feedback.
#  Default: ''
# c.CourseDirectory.student_id_exclude = ''

## The name of the directory that contains assignments that have been submitted
#  by students for grading. This corresponds to the `nbgrader_step` variable in
#  the `directory_structure` config option.
#  Default: 'submitted'
# c.CourseDirectory.submitted_directory = 'submitted'

#------------------------------------------------------------------------------
# Authenticator(LoggingConfigurable) configuration
#------------------------------------------------------------------------------
## A plugin for different authentication methods.
#  Default: 'nbgrader.auth.base.NoAuthPlugin'
# c.Authenticator.plugin_class = 'nbgrader.auth.base.NoAuthPlugin'

#------------------------------------------------------------------------------
# ExportPlugin(BasePlugin) configuration
#------------------------------------------------------------------------------
## Base class for export plugins.

## list of assignments to export
#  Default: []
# c.ExportPlugin.assignment = []

## list of students to export
#  Default: []
# c.ExportPlugin.student = []

## destination to export to
#  Default: ''
# c.ExportPlugin.to = ''

#------------------------------------------------------------------------------
# CsvExportPlugin(ExportPlugin) configuration
#------------------------------------------------------------------------------
## CSV exporter plugin.

## list of assignments to export
#  See also: ExportPlugin.assignment
# c.CsvExportPlugin.assignment = []

## list of students to export
#  See also: ExportPlugin.student
# c.CsvExportPlugin.student = []

## destination to export to
#  See also: ExportPlugin.to
# c.CsvExportPlugin.to = ''

#------------------------------------------------------------------------------
# ExtractorPlugin(BasePlugin) configuration
#------------------------------------------------------------------------------
## Submission archive files extractor plugin for the
#  :class:`~nbgrader.apps.zipcollectapp.ZipCollectApp`. Extractor plugin
#  subclasses MUST inherit from this class.

## Force overwrite of existing files.
#  Default: False
# c.ExtractorPlugin.force = False

## List of valid archive (zip) filename extensions to extract. Any archive (zip)
#  files with an extension not in this list are copied to the
#  `extracted_directory`.
#  Default: ['.zip', '.gz']
# c.ExtractorPlugin.zip_ext = ['.zip', '.gz']

#------------------------------------------------------------------------------
# FileNameCollectorPlugin(BasePlugin) configuration
#------------------------------------------------------------------------------
## Submission filename collector plugin for the
#  :class:`~nbgrader.apps.zipcollectapp.ZipCollectApp`. Collect plugin subclasses
#  MUST inherit from this class.

## This regular expression is applied to each submission filename and MUST be
#  supplied by the instructor. This regular expression MUST provide the
#  `(?P<student_id>...)` and `(?P<file_id>...)` named group expressions.
#  Optionally this regular expression can also provide the `(?P<first_name>...)`,
#  `(?P<last_name>...)`, `(?P<email>...)`, and `(?P<timestamp>...)` named group
#  expressions. For example if the filename is:
#  
#      `ps1_bitdiddle_attempt_2016-01-30-15-00-00_problem1.ipynb`
#  
#  then this `named_regexp` could be:
#  
#      ".*_(?P<student_id>\w+)_attempt_(?P<timestamp>[0-9\-]+)_(?P<file_id>\w+)"
#  
#  For named group regular expression examples see
#  https://docs.python.org/3/howto/regex.html
#  Default: ''
# c.FileNameCollectorPlugin.named_regexp = ''

## List of valid submission filename extensions to collect. Any submitted file
#  with an extension not in this list is skipped.
#  Default: ['.ipynb']
# c.FileNameCollectorPlugin.valid_ext = ['.ipynb']

#------------------------------------------------------------------------------
# LateSubmissionPlugin(BasePlugin) configuration
#------------------------------------------------------------------------------
## Predefined methods for assigning penalties for late submission

## The method for assigning late submission penalties:
#      'none': do nothing (no penalty assigned)
#      'zero': assign an overall score of zero (penalty = score)
#  Choices: any of ['none', 'zero']
#  Default: 'none'
# c.LateSubmissionPlugin.penalty_method = 'none'

#------------------------------------------------------------------------------
# NbConvertBase(LoggingConfigurable) configuration
#------------------------------------------------------------------------------
## Global configurable class for shared config
#  
#  Useful for display data priority that might be used by many transformers

## Deprecated default highlight language as of 5.0, please use language_info
#  metadata instead
#  Default: 'ipython'
# c.NbConvertBase.default_language = 'ipython'

## An ordered list of preferred output type, the first encountered will usually
#  be used when converting discarding the others.
#  Default: ['text/html', 'application/pdf', 'text/latex', 'image/svg+xml', 'image/png', 'image/jpeg', 'text/markdown', 'text/plain']
# c.NbConvertBase.display_data_priority = ['text/html', 'application/pdf', 'text/latex', 'image/svg+xml', 'image/png', 'image/jpeg', 'text/markdown', 'text/plain']

#------------------------------------------------------------------------------
# Preprocessor(NbConvertBase) configuration
#------------------------------------------------------------------------------
## A configurable preprocessor
#  
#  Inherit from this class if you wish to have configurability for your
#  preprocessor.
#  
#  Any configurable traitlets this class exposed will be configurable in profiles
#  using c.SubClassName.attribute = value
#  
#  You can overwrite `preprocess_cell()` to apply a transformation independently
#  on each cell or `preprocess()` if you prefer your own logic. See corresponding
#  docstring for information.
#  
#  Disabled by default and can be enabled via the config by
#      'c.YourPreprocessorName.enabled = True'

## Deprecated default highlight language as of 5.0, please use language_info
#  metadata instead
#  See also: NbConvertBase.default_language
# c.Preprocessor.default_language = 'ipython'

## 
#  See also: NbConvertBase.display_data_priority
# c.Preprocessor.display_data_priority = ['text/html', 'application/pdf', 'text/latex', 'image/svg+xml', 'image/png', 'image/jpeg', 'text/markdown', 'text/plain']

#  Default: False
# c.Preprocessor.enabled = False

#------------------------------------------------------------------------------
# NbGraderPreprocessor(Preprocessor) configuration
#------------------------------------------------------------------------------
## Whether to use this preprocessor when running nbgrader
#  Default: True
# c.NbGraderPreprocessor.enabled = True

#------------------------------------------------------------------------------
# AssignLatePenalties(NbGraderPreprocessor) configuration
#------------------------------------------------------------------------------
## Preprocessor for assigning penalties for late submissions to the database

## Whether to use this preprocessor when running nbgrader
#  See also: NbGraderPreprocessor.enabled
# c.AssignLatePenalties.enabled = True

## The plugin class for assigning the late penalty for each notebook.
#  Default: 'nbgrader.plugins.latesubmission.LateSubmissionPlugin'
# c.AssignLatePenalties.plugin_class = 'nbgrader.plugins.latesubmission.LateSubmissionPlugin'

#------------------------------------------------------------------------------
# IncludeHeaderFooter(NbGraderPreprocessor) configuration
#------------------------------------------------------------------------------
## A preprocessor for adding header and/or footer cells to a notebook.

## Whether to use this preprocessor when running nbgrader
#  See also: NbGraderPreprocessor.enabled
# c.IncludeHeaderFooter.enabled = True

## Path to footer notebook, relative to the root of the course directory
#  Default: ''
# c.IncludeHeaderFooter.footer = ''

## Path to header notebook, relative to the root of the course directory
#  Default: ''
# c.IncludeHeaderFooter.header = ''

#------------------------------------------------------------------------------
# LockCells(NbGraderPreprocessor) configuration
#------------------------------------------------------------------------------
## A preprocessor for making cells undeletable.

## Whether to use this preprocessor when running nbgrader
#  See also: NbGraderPreprocessor.enabled
# c.LockCells.enabled = True

## Whether all assignment cells are locked (non-deletable and non-editable)
#  Default: False
# c.LockCells.lock_all_cells = False

## Whether grade cells are locked (non-deletable)
#  Default: True
# c.LockCells.lock_grade_cells = True

## Whether readonly cells are locked (non-deletable and non-editable)
#  Default: True
# c.LockCells.lock_readonly_cells = True

## Whether solution cells are locked (non-deletable and non-editable)
#  Default: True
# c.LockCells.lock_solution_cells = True

#------------------------------------------------------------------------------
# ClearSolutions(NbGraderPreprocessor) configuration
#------------------------------------------------------------------------------
## The delimiter marking the beginning of a solution
#  Default: 'BEGIN SOLUTION'
# c.ClearSolutions.begin_solution_delimeter = 'BEGIN SOLUTION'

## The code snippet that will replace code solutions
#  Default: {'python': '# YOUR CODE HERE\nraise NotImplementedError()', 'matlab': "% YOUR CODE HERE\nerror('No Answer Given!')", 'octave': "% YOUR CODE HERE\nerror('No Answer Given!')", 'java': '// YOUR CODE HERE'}
# c.ClearSolutions.code_stub = {'python': '# YOUR CODE HERE\nraise NotImplementedError()', 'matlab': "% YOUR CODE HERE\nerror('No Answer Given!')", 'octave': "% YOUR CODE HERE\nerror('No Answer Given!')", 'java': '// YOUR CODE HERE'}

## Whether to use this preprocessor when running nbgrader
#  See also: NbGraderPreprocessor.enabled
# c.ClearSolutions.enabled = True

## The delimiter marking the end of a solution
#  Default: 'END SOLUTION'
# c.ClearSolutions.end_solution_delimeter = 'END SOLUTION'

## Whether or not to complain if cells containing solutions regions are not
#  marked as solution cells. WARNING: this will potentially cause things to break
#  if you are using the full nbgrader pipeline. ONLY disable this option if you
#  are only ever planning to use nbgrader assign.
#  Default: True
# c.ClearSolutions.enforce_metadata = True

## The text snippet that will replace written solutions
#  Default: 'YOUR ANSWER HERE'
# c.ClearSolutions.text_stub = 'YOUR ANSWER HERE'

#------------------------------------------------------------------------------
# SaveAutoGrades(NbGraderPreprocessor) configuration
#------------------------------------------------------------------------------
## Preprocessor for saving out the autograder grades into a database

## Whether to use this preprocessor when running nbgrader
#  See also: NbGraderPreprocessor.enabled
# c.SaveAutoGrades.enabled = True

#------------------------------------------------------------------------------
# ComputeChecksums(NbGraderPreprocessor) configuration
#------------------------------------------------------------------------------
## A preprocessor to compute checksums of grade cells.

## Whether to use this preprocessor when running nbgrader
#  See also: NbGraderPreprocessor.enabled
# c.ComputeChecksums.enabled = True

#------------------------------------------------------------------------------
# SaveCells(NbGraderPreprocessor) configuration
#------------------------------------------------------------------------------
## A preprocessor to save information about grade and solution cells.

## Whether to use this preprocessor when running nbgrader
#  See also: NbGraderPreprocessor.enabled
# c.SaveCells.enabled = True

#------------------------------------------------------------------------------
# OverwriteCells(NbGraderPreprocessor) configuration
#------------------------------------------------------------------------------
## A preprocessor to overwrite information about grade and solution cells.

## Whether to use this preprocessor when running nbgrader
#  See also: NbGraderPreprocessor.enabled
# c.OverwriteCells.enabled = True

#------------------------------------------------------------------------------
# CheckCellMetadata(NbGraderPreprocessor) configuration
#------------------------------------------------------------------------------
## A preprocessor for checking that grade ids are unique.

## Whether to use this preprocessor when running nbgrader
#  See also: NbGraderPreprocessor.enabled
# c.CheckCellMetadata.enabled = True

#------------------------------------------------------------------------------
# NotebookClient(LoggingConfigurable) configuration
#------------------------------------------------------------------------------
## Encompasses a Client for executing cells in a notebook

## If ``False`` (default), when a cell raises an error the execution is stopped
#  and a `CellExecutionError` is raised. If ``True``, execution errors are
#  ignored and the execution is continued until the end of the notebook. Output
#  from exceptions is included in the cell output in both cases.
#  Default: False
# c.NotebookClient.allow_errors = False

## An ordered list of preferred output type, the first encountered will usually
#  be used when converting discarding the others.
#  Default: ['text/html', 'application/pdf', 'text/latex', 'image/svg+xml', 'image/png', 'image/jpeg', 'text/markdown', 'text/plain']
# c.NotebookClient.display_data_priority = ['text/html', 'application/pdf', 'text/latex', 'image/svg+xml', 'image/png', 'image/jpeg', 'text/markdown', 'text/plain']

#  Default: []
# c.NotebookClient.extra_arguments = []

## If False (default), errors from executing the notebook can be allowed with a
#  ``raises-exception`` tag on a single cell, or the ``allow_errors``
#  configurable option for all cells. An allowed error will be recorded in
#  notebook output, and execution will continue. If an error occurs when it is
#  not explicitly allowed, a `CellExecutionError` will be raised. If True,
#  `CellExecutionError` will be raised for any error that occurs while executing
#  the notebook. This overrides both the ``allow_errors`` option and the
#  ``raises-exception`` cell tag.
#  Default: False
# c.NotebookClient.force_raise_errors = False

## If execution of a cell times out, interrupt the kernel and continue executing
#  other cells rather than throwing an error and stopping.
#  Default: False
# c.NotebookClient.interrupt_on_timeout = False

## The time to wait (in seconds) for IOPub output. This generally doesn't need to
#  be set, but on some slow networks (such as CI systems) the default timeout
#  might not be long enough to get all messages.
#  Default: 4
# c.NotebookClient.iopub_timeout = 4

## Path to file to use for SQLite history database for an IPython kernel.
#  
#  The specific value ``:memory:`` (including the colon at both end but not the
#  back ticks), avoids creating a history file. Otherwise, IPython will create a
#  history file for each kernel.
#  
#  When running kernels simultaneously (e.g. via multiprocessing) saving history
#  a single SQLite file can result in database errors, so using ``:memory:`` is
#  recommended in non-interactive contexts.
#  Default: ':memory:'
# c.NotebookClient.ipython_hist_file = ':memory:'

## The kernel manager class to use.
#  Default: 'builtins.object'
# c.NotebookClient.kernel_manager_class = 'builtins.object'

## Name of kernel to use to execute the cells. If not set, use the kernel_spec
#  embedded in the notebook.
#  Default: ''
# c.NotebookClient.kernel_name = ''

## If ``False`` (default), then the kernel will continue waiting for iopub
#  messages until it receives a kernel idle message, or until a timeout occurs,
#  at which point the currently executing cell will be skipped. If ``True``, then
#  an error will be raised after the first timeout. This option generally does
#  not need to be used, but may be useful in contexts where there is the
#  possibility of executing notebooks with memory-consuming infinite loops.
#  Default: False
# c.NotebookClient.raise_on_iopub_timeout = False

## If ``True`` (default), then the execution timings of each cell will be stored
#  in the metadata of the notebook.
#  Default: True
# c.NotebookClient.record_timing = True

## The time to wait (in seconds) for Shell output before retrying. This generally
#  doesn't need to be set, but if one needs to check for dead kernels at a faster
#  rate this can help.
#  Default: 5
# c.NotebookClient.shell_timeout_interval = 5

## If ``graceful`` (default), then the kernel is given time to clean up after
#  executing all cells, e.g., to execute its ``atexit`` hooks. If ``immediate``,
#  then the kernel is signaled to immediately terminate.
#  Choices: any of ['graceful', 'immediate']
#  Default: 'graceful'
# c.NotebookClient.shutdown_kernel = 'graceful'

## The time to wait (in seconds) for the kernel to start. If kernel startup takes
#  longer, a RuntimeError is raised.
#  Default: 60
# c.NotebookClient.startup_timeout = 60

## If ``True`` (default), then the state of the Jupyter widgets created at the
#  kernel will be stored in the metadata of the notebook.
#  Default: True
# c.NotebookClient.store_widget_state = True

## The time to wait (in seconds) for output from executions. If a cell execution
#  takes longer, a TimeoutError is raised.
#  
#  ``None`` or ``-1`` will disable the timeout. If ``timeout_func`` is set, it
#  overrides ``timeout``.
#  Default: None
# c.NotebookClient.timeout = None

## A callable which, when given the cell source as input, returns the time to
#  wait (in seconds) for output from cell executions. If a cell execution takes
#  longer, a TimeoutError is raised.
#  
#  Returning ``None`` or ``-1`` will disable the timeout for the cell. Not
#  setting ``timeout_func`` will cause the preprocessor to default to using the
#  ``timeout`` trait for all cells. The ``timeout_func`` trait overrides
#  ``timeout`` if it is not ``None``.
#  Default: None
# c.NotebookClient.timeout_func = None

#------------------------------------------------------------------------------
# ExecutePreprocessor(Preprocessor, NotebookClient) configuration
#------------------------------------------------------------------------------
## Executes all the cells in a notebook

## 
#  See also: NotebookClient.allow_errors
# c.ExecutePreprocessor.allow_errors = False

## Deprecated default highlight language as of 5.0, please use language_info
#  metadata instead
#  See also: NbConvertBase.default_language
# c.ExecutePreprocessor.default_language = 'ipython'

## 
#  See also: NbConvertBase.display_data_priority
# c.ExecutePreprocessor.display_data_priority = ['text/html', 'application/pdf', 'text/latex', 'image/svg+xml', 'image/png', 'image/jpeg', 'text/markdown', 'text/plain']

#  See also: Preprocessor.enabled
# c.ExecutePreprocessor.enabled = False

#  See also: NotebookClient.extra_arguments
# c.ExecutePreprocessor.extra_arguments = []

## 
#  See also: NotebookClient.force_raise_errors
# c.ExecutePreprocessor.force_raise_errors = False

## 
#  See also: NotebookClient.interrupt_on_timeout
# c.ExecutePreprocessor.interrupt_on_timeout = False

## 
#  See also: NotebookClient.iopub_timeout
# c.ExecutePreprocessor.iopub_timeout = 4

## Path to file to use for SQLite history database for an IPython kernel.
#  See also: NotebookClient.ipython_hist_file
# c.ExecutePreprocessor.ipython_hist_file = ':memory:'

## The kernel manager class to use.
#  See also: NotebookClient.kernel_manager_class
# c.ExecutePreprocessor.kernel_manager_class = 'builtins.object'

## 
#  See also: NotebookClient.kernel_name
# c.ExecutePreprocessor.kernel_name = ''

## 
#  See also: NotebookClient.raise_on_iopub_timeout
# c.ExecutePreprocessor.raise_on_iopub_timeout = False

## 
#  See also: NotebookClient.record_timing
# c.ExecutePreprocessor.record_timing = True

## 
#  See also: NotebookClient.shell_timeout_interval
# c.ExecutePreprocessor.shell_timeout_interval = 5

## 
#  See also: NotebookClient.shutdown_kernel
# c.ExecutePreprocessor.shutdown_kernel = 'graceful'

## 
#  See also: NotebookClient.startup_timeout
# c.ExecutePreprocessor.startup_timeout = 60

## 
#  See also: NotebookClient.store_widget_state
# c.ExecutePreprocessor.store_widget_state = True

## 
#  See also: NotebookClient.timeout
# c.ExecutePreprocessor.timeout = None

## 
#  See also: NotebookClient.timeout_func
# c.ExecutePreprocessor.timeout_func = None

#------------------------------------------------------------------------------
# Execute(NbGraderPreprocessor, ExecutePreprocessor) configuration
#------------------------------------------------------------------------------
## Whether to use this preprocessor when running nbgrader
#  See also: NbGraderPreprocessor.enabled
# c.Execute.enabled = True

## The number of times to try re-executing the notebook before throwing an error.
#  Generally, this shouldn't need to be set, but might be useful for CI
#  environments when tests are flaky.
#  Default: 0
# c.Execute.execute_retries = 0

## A list of extra arguments to pass to the kernel. For python kernels, this
#  defaults to ``--HistoryManager.hist_file=:memory:``. For other kernels this is
#  just an empty list.
#  Default: []
# c.Execute.extra_arguments = []

## 
#  See also: NotebookClient.force_raise_errors
# c.Execute.force_raise_errors = False

## 
#  See also: NotebookClient.iopub_timeout
# c.Execute.iopub_timeout = 4

## Path to file to use for SQLite history database for an IPython kernel.
#  See also: NotebookClient.ipython_hist_file
# c.Execute.ipython_hist_file = ':memory:'

## The kernel manager class to use.
#  See also: NotebookClient.kernel_manager_class
# c.Execute.kernel_manager_class = 'builtins.object'

## 
#  See also: NotebookClient.kernel_name
# c.Execute.kernel_name = ''

## 
#  See also: NotebookClient.record_timing
# c.Execute.record_timing = True

## 
#  See also: NotebookClient.shell_timeout_interval
# c.Execute.shell_timeout_interval = 5

## 
#  See also: NotebookClient.shutdown_kernel
# c.Execute.shutdown_kernel = 'graceful'

## 
#  See also: NotebookClient.startup_timeout
# c.Execute.startup_timeout = 60

## 
#  See also: NotebookClient.store_widget_state
# c.Execute.store_widget_state = True

## 
#  See also: NotebookClient.timeout
# c.Execute.timeout = None

## 
#  See also: NotebookClient.timeout_func
# c.Execute.timeout_func = None

#------------------------------------------------------------------------------
# GetGrades(NbGraderPreprocessor) configuration
#------------------------------------------------------------------------------
## Preprocessor for saving grades from the database to the notebook

#  Default: ['text/html', 'application/pdf', 'text/latex', 'image/svg+xml', 'image/png', 'image/jpeg', 'text/plain']
# c.GetGrades.display_data_priority = ['text/html', 'application/pdf', 'text/latex', 'image/svg+xml', 'image/png', 'image/jpeg', 'text/plain']

## Whether to use this preprocessor when running nbgrader
#  See also: NbGraderPreprocessor.enabled
# c.GetGrades.enabled = True

#------------------------------------------------------------------------------
# ClearOutputPreprocessor(Preprocessor) configuration
#------------------------------------------------------------------------------
## Removes the output from all code cells in a notebook.

## Deprecated default highlight language as of 5.0, please use language_info
#  metadata instead
#  See also: NbConvertBase.default_language
# c.ClearOutputPreprocessor.default_language = 'ipython'

## 
#  See also: NbConvertBase.display_data_priority
# c.ClearOutputPreprocessor.display_data_priority = ['text/html', 'application/pdf', 'text/latex', 'image/svg+xml', 'image/png', 'image/jpeg', 'text/markdown', 'text/plain']

#  See also: Preprocessor.enabled
# c.ClearOutputPreprocessor.enabled = False

#  Default: {'collapsed', 'scrolled'}
# c.ClearOutputPreprocessor.remove_metadata_fields = {'collapsed', 'scrolled'}

#------------------------------------------------------------------------------
# ClearOutput(NbGraderPreprocessor, ClearOutputPreprocessor) configuration
#------------------------------------------------------------------------------
## Whether to use this preprocessor when running nbgrader
#  See also: NbGraderPreprocessor.enabled
# c.ClearOutput.enabled = True

#  See also: ClearOutputPreprocessor.remove_metadata_fields
# c.ClearOutput.remove_metadata_fields = {'collapsed', 'scrolled'}

#------------------------------------------------------------------------------
# LimitOutput(NbGraderPreprocessor) configuration
#------------------------------------------------------------------------------
## Preprocessor for limiting cell output

## Whether to use this preprocessor when running nbgrader
#  See also: NbGraderPreprocessor.enabled
# c.LimitOutput.enabled = True

## maximum number of lines of output (-1 means no limit)
#  Default: 1000
# c.LimitOutput.max_lines = 1000

## maximum number of traceback lines (-1 means no limit)
#  Default: 100
# c.LimitOutput.max_traceback = 100

#------------------------------------------------------------------------------
# DeduplicateIds(NbGraderPreprocessor) configuration
#------------------------------------------------------------------------------
## A preprocessor to overwrite information about grade and solution cells.

## Whether to use this preprocessor when running nbgrader
#  See also: NbGraderPreprocessor.enabled
# c.DeduplicateIds.enabled = True

#------------------------------------------------------------------------------
# ClearHiddenTests(NbGraderPreprocessor) configuration
#------------------------------------------------------------------------------
## The delimiter marking the beginning of hidden tests cases
#  Default: 'BEGIN HIDDEN TESTS'
# c.ClearHiddenTests.begin_test_delimeter = 'BEGIN HIDDEN TESTS'

## Whether to use this preprocessor when running nbgrader
#  See also: NbGraderPreprocessor.enabled
# c.ClearHiddenTests.enabled = True

## The delimiter marking the end of hidden tests cases
#  Default: 'END HIDDEN TESTS'
# c.ClearHiddenTests.end_test_delimeter = 'END HIDDEN TESTS'

## Whether or not to complain if cells containing hidden test regions are not
#  marked as grade cells. WARNING: this will potentially cause things to break if
#  you are using the full nbgrader pipeline. ONLY disable this option if you are
#  only ever planning to use nbgrader assign.
#  Default: True
# c.ClearHiddenTests.enforce_metadata = True

#------------------------------------------------------------------------------
# ClearMarkScheme(NbGraderPreprocessor) configuration
#------------------------------------------------------------------------------
## The delimiter marking the beginning of hidden tests cases
#  Default: 'BEGIN MARK SCHEME'
# c.ClearMarkScheme.begin_mark_scheme_delimeter = 'BEGIN MARK SCHEME'

## Whether to use this preprocessor when running nbgrader
#  See also: NbGraderPreprocessor.enabled
# c.ClearMarkScheme.enabled = True

## The delimiter marking the end of hidden tests cases
#  Default: 'END MARK SCHEME'
# c.ClearMarkScheme.end_mark_scheme_delimeter = 'END MARK SCHEME'

## Whether or not to complain if cells containing marking scheme regions are not
#  marked as task cells. WARNING: this will potentially cause things to break if
#  you are using the full nbgrader pipeline. ONLY disable this option if you are
#  only ever planning to use nbgrader assign.
#  Default: True
# c.ClearMarkScheme.enforce_metadata = True

#------------------------------------------------------------------------------
# OverwriteKernelspec(NbGraderPreprocessor) configuration
#------------------------------------------------------------------------------
## A preprocessor for checking the notebook kernelspec metadata.

## Whether to use this preprocessor when running nbgrader
#  See also: NbGraderPreprocessor.enabled
# c.OverwriteKernelspec.enabled = True

#------------------------------------------------------------------------------
# Exchange(LoggingConfigurable) configuration
#------------------------------------------------------------------------------
## Local path for storing student assignments.  Defaults to '.' which is normally
#  Jupyter's notebook_dir.
#  Default: '.'
# c.Exchange.assignment_dir = '.'

## Local cache directory for nbgrader submit and nbgrader list. Defaults to
#  $JUPYTER_DATA_DIR/nbgrader_cache
#  Default: ''
# c.Exchange.cache = ''

## Whether the path for fetching/submitting  assignments should be prefixed with
#  the course name. If this is `False`, then the path will be something like
#  `./ps1`. If this is `True`, then the path will be something like
#  `./course123/ps1`.
#  Default: False
# c.Exchange.path_includes_course = False

## The nbgrader exchange directory writable to everyone. MUST be preexisting.
#  Default: '/srv/nbgrader/exchange'
# c.Exchange.root = '/srv/nbgrader/exchange'

## Format string for timestamps
#  Default: '%Y-%m-%d %H:%M:%S.%f %Z'
# c.Exchange.timestamp_format = '%Y-%m-%d %H:%M:%S.%f %Z'

## Timezone for recording timestamps
#  Default: 'UTC'
# c.Exchange.timezone = 'UTC'

#------------------------------------------------------------------------------
# ExchangeCollect(Exchange) configuration
#------------------------------------------------------------------------------
## 
#  See also: Exchange.assignment_dir
# c.ExchangeCollect.assignment_dir = '.'

## Local cache directory for nbgrader submit and nbgrader list. Defaults to
#  $JUPYTER_DATA_DIR/nbgrader_cache
#  See also: Exchange.cache
# c.ExchangeCollect.cache = ''

## Whether to cross-check the student_id with the UNIX-owner of the submitted
#  directory.
#  Default: True
# c.ExchangeCollect.check_owner = True

## 
#  See also: Exchange.path_includes_course
# c.ExchangeCollect.path_includes_course = False

## The nbgrader exchange directory writable to everyone. MUST be preexisting.
#  See also: Exchange.root
# c.ExchangeCollect.root = '/srv/nbgrader/exchange'

## Format string for timestamps
#  See also: Exchange.timestamp_format
# c.ExchangeCollect.timestamp_format = '%Y-%m-%d %H:%M:%S.%f %Z'

## Timezone for recording timestamps
#  See also: Exchange.timezone
# c.ExchangeCollect.timezone = 'UTC'

## Update existing submissions with ones that have newer timestamps.
#  Default: False
# c.ExchangeCollect.update = False

#------------------------------------------------------------------------------
# ExchangeFetchAssignment(Exchange) configuration
#------------------------------------------------------------------------------
## 
#  See also: Exchange.assignment_dir
# c.ExchangeFetchAssignment.assignment_dir = '.'

## Local cache directory for nbgrader submit and nbgrader list. Defaults to
#  $JUPYTER_DATA_DIR/nbgrader_cache
#  See also: Exchange.cache
# c.ExchangeFetchAssignment.cache = ''

## 
#  See also: Exchange.path_includes_course
# c.ExchangeFetchAssignment.path_includes_course = False

## Whether to replace missing files on fetch
#  Default: False
# c.ExchangeFetchAssignment.replace_missing_files = False

## The nbgrader exchange directory writable to everyone. MUST be preexisting.
#  See also: Exchange.root
# c.ExchangeFetchAssignment.root = '/srv/nbgrader/exchange'

## Format string for timestamps
#  See also: Exchange.timestamp_format
# c.ExchangeFetchAssignment.timestamp_format = '%Y-%m-%d %H:%M:%S.%f %Z'

## Timezone for recording timestamps
#  See also: Exchange.timezone
# c.ExchangeFetchAssignment.timezone = 'UTC'

#------------------------------------------------------------------------------
# ExchangeFetch(ExchangeFetchAssignment) configuration
#------------------------------------------------------------------------------
## 
#  See also: Exchange.assignment_dir
# c.ExchangeFetch.assignment_dir = '.'

## Local cache directory for nbgrader submit and nbgrader list. Defaults to
#  $JUPYTER_DATA_DIR/nbgrader_cache
#  See also: Exchange.cache
# c.ExchangeFetch.cache = ''

## 
#  See also: Exchange.path_includes_course
# c.ExchangeFetch.path_includes_course = False

## Whether to replace missing files on fetch
#  See also: ExchangeFetchAssignment.replace_missing_files
# c.ExchangeFetch.replace_missing_files = False

## The nbgrader exchange directory writable to everyone. MUST be preexisting.
#  See also: Exchange.root
# c.ExchangeFetch.root = '/srv/nbgrader/exchange'

## Format string for timestamps
#  See also: Exchange.timestamp_format
# c.ExchangeFetch.timestamp_format = '%Y-%m-%d %H:%M:%S.%f %Z'

## Timezone for recording timestamps
#  See also: Exchange.timezone
# c.ExchangeFetch.timezone = 'UTC'

#------------------------------------------------------------------------------
# ExchangeFetchFeedback(Exchange) configuration
#------------------------------------------------------------------------------
## 
#  See also: Exchange.assignment_dir
# c.ExchangeFetchFeedback.assignment_dir = '.'

## Local cache directory for nbgrader submit and nbgrader list. Defaults to
#  $JUPYTER_DATA_DIR/nbgrader_cache
#  See also: Exchange.cache
# c.ExchangeFetchFeedback.cache = ''

## 
#  See also: Exchange.path_includes_course
# c.ExchangeFetchFeedback.path_includes_course = False

## The nbgrader exchange directory writable to everyone. MUST be preexisting.
#  See also: Exchange.root
# c.ExchangeFetchFeedback.root = '/srv/nbgrader/exchange'

## Format string for timestamps
#  See also: Exchange.timestamp_format
# c.ExchangeFetchFeedback.timestamp_format = '%Y-%m-%d %H:%M:%S.%f %Z'

## Timezone for recording timestamps
#  See also: Exchange.timezone
# c.ExchangeFetchFeedback.timezone = 'UTC'

#------------------------------------------------------------------------------
# ExchangeList(Exchange) configuration
#------------------------------------------------------------------------------
## 
#  See also: Exchange.assignment_dir
# c.ExchangeList.assignment_dir = '.'

## Local cache directory for nbgrader submit and nbgrader list. Defaults to
#  $JUPYTER_DATA_DIR/nbgrader_cache
#  See also: Exchange.cache
# c.ExchangeList.cache = ''

## List assignments in submission cache.
#  Default: False
# c.ExchangeList.cached = False

## List inbound files rather than outbound.
#  Default: False
# c.ExchangeList.inbound = False

## 
#  See also: Exchange.path_includes_course
# c.ExchangeList.path_includes_course = False

## Remove, rather than list files.
#  Default: False
# c.ExchangeList.remove = False

## The nbgrader exchange directory writable to everyone. MUST be preexisting.
#  See also: Exchange.root
# c.ExchangeList.root = '/srv/nbgrader/exchange'

## Format string for timestamps
#  See also: Exchange.timestamp_format
# c.ExchangeList.timestamp_format = '%Y-%m-%d %H:%M:%S.%f %Z'

## Timezone for recording timestamps
#  See also: Exchange.timezone
# c.ExchangeList.timezone = 'UTC'

#------------------------------------------------------------------------------
# ExchangeReleaseAssignment(Exchange) configuration
#------------------------------------------------------------------------------
## 
#  See also: Exchange.assignment_dir
# c.ExchangeReleaseAssignment.assignment_dir = '.'

## Local cache directory for nbgrader submit and nbgrader list. Defaults to
#  $JUPYTER_DATA_DIR/nbgrader_cache
#  See also: Exchange.cache
# c.ExchangeReleaseAssignment.cache = ''

## Force overwrite existing files in the exchange.
#  Default: False
# c.ExchangeReleaseAssignment.force = False

## 
#  See also: Exchange.path_includes_course
# c.ExchangeReleaseAssignment.path_includes_course = False

## The nbgrader exchange directory writable to everyone. MUST be preexisting.
#  See also: Exchange.root
# c.ExchangeReleaseAssignment.root = '/srv/nbgrader/exchange'

## Format string for timestamps
#  See also: Exchange.timestamp_format
# c.ExchangeReleaseAssignment.timestamp_format = '%Y-%m-%d %H:%M:%S.%f %Z'

## Timezone for recording timestamps
#  See also: Exchange.timezone
# c.ExchangeReleaseAssignment.timezone = 'UTC'

#------------------------------------------------------------------------------
# ExchangeRelease(ExchangeReleaseAssignment) configuration
#------------------------------------------------------------------------------
## 
#  See also: Exchange.assignment_dir
# c.ExchangeRelease.assignment_dir = '.'

## Local cache directory for nbgrader submit and nbgrader list. Defaults to
#  $JUPYTER_DATA_DIR/nbgrader_cache
#  See also: Exchange.cache
# c.ExchangeRelease.cache = ''

## Force overwrite existing files in the exchange.
#  See also: ExchangeReleaseAssignment.force
# c.ExchangeRelease.force = False

## 
#  See also: Exchange.path_includes_course
# c.ExchangeRelease.path_includes_course = False

## The nbgrader exchange directory writable to everyone. MUST be preexisting.
#  See also: Exchange.root
# c.ExchangeRelease.root = '/srv/nbgrader/exchange'

## Format string for timestamps
#  See also: Exchange.timestamp_format
# c.ExchangeRelease.timestamp_format = '%Y-%m-%d %H:%M:%S.%f %Z'

## Timezone for recording timestamps
#  See also: Exchange.timezone
# c.ExchangeRelease.timezone = 'UTC'

#------------------------------------------------------------------------------
# ExchangeReleaseFeedback(Exchange) configuration
#------------------------------------------------------------------------------
## 
#  See also: Exchange.assignment_dir
# c.ExchangeReleaseFeedback.assignment_dir = '.'

## Local cache directory for nbgrader submit and nbgrader list. Defaults to
#  $JUPYTER_DATA_DIR/nbgrader_cache
#  See also: Exchange.cache
# c.ExchangeReleaseFeedback.cache = ''

## 
#  See also: Exchange.path_includes_course
# c.ExchangeReleaseFeedback.path_includes_course = False

## The nbgrader exchange directory writable to everyone. MUST be preexisting.
#  See also: Exchange.root
# c.ExchangeReleaseFeedback.root = '/srv/nbgrader/exchange'

## Format string for timestamps
#  See also: Exchange.timestamp_format
# c.ExchangeReleaseFeedback.timestamp_format = '%Y-%m-%d %H:%M:%S.%f %Z'

## Timezone for recording timestamps
#  See also: Exchange.timezone
# c.ExchangeReleaseFeedback.timezone = 'UTC'

#------------------------------------------------------------------------------
# ExchangeSubmit(Exchange) configuration
#------------------------------------------------------------------------------
## Whether to add a random string on the end of the submission.
#  Default: True
# c.ExchangeSubmit.add_random_string = True

## 
#  See also: Exchange.assignment_dir
# c.ExchangeSubmit.assignment_dir = '.'

## Local cache directory for nbgrader submit and nbgrader list. Defaults to
#  $JUPYTER_DATA_DIR/nbgrader_cache
#  See also: Exchange.cache
# c.ExchangeSubmit.cache = ''

## 
#  See also: Exchange.path_includes_course
# c.ExchangeSubmit.path_includes_course = False

## The nbgrader exchange directory writable to everyone. MUST be preexisting.
#  See also: Exchange.root
# c.ExchangeSubmit.root = '/srv/nbgrader/exchange'

## Whether or not to submit the assignment if there are missing notebooks from
#  the released assignment notebooks.
#  Default: False
# c.ExchangeSubmit.strict = False

## Format string for timestamps
#  See also: Exchange.timestamp_format
# c.ExchangeSubmit.timestamp_format = '%Y-%m-%d %H:%M:%S.%f %Z'

## Timezone for recording timestamps
#  See also: Exchange.timezone
# c.ExchangeSubmit.timezone = 'UTC'

#------------------------------------------------------------------------------
# BaseConverter(LoggingConfigurable) configuration
#------------------------------------------------------------------------------
## Whether to overwrite existing assignments/submissions
#  Default: False
# c.BaseConverter.force = False

## Permissions to set on files output by nbgrader. The default is generally read-
#  only (444), with the exception of nbgrader generate_assignment and nbgrader
#  generate_feedback, in which case the user also has write permission.
#  Default: 0
# c.BaseConverter.permissions = 0

#------------------------------------------------------------------------------
# GenerateAssignment(BaseConverter) configuration
#------------------------------------------------------------------------------
## Whether to create the assignment at runtime if it does not already exist.
#  Default: True
# c.GenerateAssignment.create_assignment = True

## Whether to overwrite existing assignments/submissions
#  See also: BaseConverter.force
# c.GenerateAssignment.force = False

## Do not save information about the assignment into the database.
#  Default: False
# c.GenerateAssignment.no_database = False

## 
#  See also: BaseConverter.permissions
# c.GenerateAssignment.permissions = 0

#------------------------------------------------------------------------------
# Assign(GenerateAssignment) configuration
#------------------------------------------------------------------------------
## 
#  See also: GenerateAssignment.create_assignment
# c.Assign.create_assignment = True

## Whether to overwrite existing assignments/submissions
#  See also: BaseConverter.force
# c.Assign.force = False

## 
#  See also: GenerateAssignment.no_database
# c.Assign.no_database = False

## 
#  See also: BaseConverter.permissions
# c.Assign.permissions = 0

#------------------------------------------------------------------------------
# Autograde(BaseConverter) configuration
#------------------------------------------------------------------------------
## Whether to create the student at runtime if it does not already exist.
#  Default: True
# c.Autograde.create_student = True

## A dictionary with keys corresponding to assignment names and values being a
#  list of filenames (relative to the assignment's source directory) that should
#  NOT be overwritten with the source version. This is to allow students to e.g.
#  edit a python file and submit it alongside the notebooks in their assignment.
#  Default: {}
# c.Autograde.exclude_overwriting = {}

## Whether to overwrite existing assignments/submissions
#  See also: BaseConverter.force
# c.Autograde.force = False

## 
#  See also: BaseConverter.permissions
# c.Autograde.permissions = 0

#------------------------------------------------------------------------------
# GenerateFeedback(BaseConverter) configuration
#------------------------------------------------------------------------------
## Whether to overwrite existing assignments/submissions
#  See also: BaseConverter.force
# c.GenerateFeedback.force = False

## 
#  See also: BaseConverter.permissions
# c.GenerateFeedback.permissions = 0

#------------------------------------------------------------------------------
# Feedback(GenerateFeedback) configuration
#------------------------------------------------------------------------------
## Whether to overwrite existing assignments/submissions
#  See also: BaseConverter.force
# c.Feedback.force = False

## 
#  See also: BaseConverter.permissions
# c.Feedback.permissions = 0
