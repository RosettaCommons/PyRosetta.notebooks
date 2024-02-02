c = get_config()

###############################################################################
# Begin additions by nbgrader quickstart
###############################################################################

# You only need this if you are running nbgrader on a shared
# server set up.
c.CourseDirectory.course_id = "student-notebooks"

c.IncludeHeaderFooter.header = "source/header.ipynb"

###############################################################################
# End additions by nbgrader quickstart
###############################################################################

# Configuration file for nbgrader-generate-config.

c = get_config()  #noqa

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

## Configure additional log handlers.
#  
#  The default stderr logs handler is configured by the log_level, log_datefmt
#  and log_format settings.
#  
#  This configuration can be used to configure additional handlers (e.g. to
#  output the log to a file) or for finer control over the default handlers.
#  
#  If provided this should be a logging configuration dictionary, for more
#  information see:
#  https://docs.python.org/3/library/logging.config.html#logging-config-
#  dictschema
#  
#  This dictionary is merged with the base logging configuration which defines
#  the following:
#  
#  * A logging formatter intended for interactive use called
#    ``console``.
#  * A logging handler that writes to stderr called
#    ``console`` which uses the formatter ``console``.
#  * A logger with the name of this application set to ``DEBUG``
#    level.
#  
#  This example adds a new handler that writes to a file:
#  
#  .. code-block:: python
#  
#     c.Application.logging_config = {
#         "handlers": {
#             "file": {
#                 "class": "logging.FileHandler",
#                 "level": "DEBUG",
#                 "filename": "<path/to/file>",
#             }
#         },
#         "loggers": {
#             "<application-name>": {
#                 "level": "DEBUG",
#                 # NOTE: if you don't list the default "console"
#                 # handler here then it will be disabled
#                 "handlers": ["console", "file"],
#             },
#         },
#     }
#  Default: {}
# c.Application.logging_config = {}

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

## 
#  See also: Application.logging_config
# c.JupyterApp.logging_config = {}

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

## 
#  See also: Application.logging_config
# c.NbGrader.logging_config = {}

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

## 
#  See also: Application.logging_config
# c.GenerateConfigApp.logging_config = {}

## Instead of starting the Application, dump configuration to stdout
#  See also: Application.show_config
# c.GenerateConfigApp.show_config = False

## Instead of starting the Application, dump configuration to stdout (as JSON)
#  See also: Application.show_config_json
# c.GenerateConfigApp.show_config_json = False

#------------------------------------------------------------------------------
# ExchangeFactory(LoggingConfigurable) configuration
#------------------------------------------------------------------------------
## A plugin for collecting assignments.
#  Default: 'nbgrader.exchange.default.collect.ExchangeCollect'
# c.ExchangeFactory.collect = 'nbgrader.exchange.default.collect.ExchangeCollect'

## A plugin for exchange.
#  Default: 'nbgrader.exchange.default.exchange.Exchange'
# c.ExchangeFactory.exchange = 'nbgrader.exchange.default.exchange.Exchange'

## A plugin for fetching assignments.
#  Default: 'nbgrader.exchange.default.fetch_assignment.ExchangeFetchAssignment'
# c.ExchangeFactory.fetch_assignment = 'nbgrader.exchange.default.fetch_assignment.ExchangeFetchAssignment'

## A plugin for fetching feedback.
#  Default: 'nbgrader.exchange.default.fetch_feedback.ExchangeFetchFeedback'
# c.ExchangeFactory.fetch_feedback = 'nbgrader.exchange.default.fetch_feedback.ExchangeFetchFeedback'

## A plugin for listing exchange files.
#  Default: 'nbgrader.exchange.default.list.ExchangeList'
# c.ExchangeFactory.list = 'nbgrader.exchange.default.list.ExchangeList'

## A plugin for releasing assignments.
#  Default: 'nbgrader.exchange.default.release_assignment.ExchangeReleaseAssignment'
# c.ExchangeFactory.release_assignment = 'nbgrader.exchange.default.release_assignment.ExchangeReleaseAssignment'

## A plugin for releasing feedback.
#  Default: 'nbgrader.exchange.default.release_feedback.ExchangeReleaseFeedback'
# c.ExchangeFactory.release_feedback = 'nbgrader.exchange.default.release_feedback.ExchangeReleaseFeedback'

## A plugin for submitting assignments.
#  Default: 'nbgrader.exchange.default.submit.ExchangeSubmit'
# c.ExchangeFactory.submit = 'nbgrader.exchange.default.submit.ExchangeSubmit'

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

## Maximum size of directories (in kilobytes; default: 100Mb). Upon copying
#  directories recursively, larger files will be ignored with a warning.
#  Default: 100000
# c.CourseDirectory.max_dir_size = 100000

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

## The name of the directory that contains the assignment solution after grading
#  has been completed. This corresponds to the `nbgrader_step` variable in the
#  `directory_structure` config option.
#  Default: 'solution'
# c.CourseDirectory.solution_directory = 'solution'

## The name of the directory that contains the master/instructor version of
#  assignments. This corresponds to the `nbgrader_step` variable in the
#  `directory_structure` config option.
#  Default: 'source'
# c.CourseDirectory.source_directory = 'source'

## The name of the directory that contains notebooks with both solutions and
#  instantiated test code (i.e., all AUTOTEST directives are removed and replaced
#  by actual test code). This corresponds to the `nbgrader_step` variable in the
#  `directory_structure` config option.
#  Default: 'source_with_tests'
# c.CourseDirectory.source_with_tests_directory = 'source_with_tests'

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
#      :class:`~nbgrader.apps.zipcollectapp.ZipCollectApp`.
#      Extractor plugin subclasses MUST inherit from this class.

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
#      :class:`~nbgrader.apps.zipcollectapp.ZipCollectApp`.
#      Collect plugin subclasses MUST inherit from this class.

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
#      Useful for display data priority that might be used by many transformers

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
#      Inherit from this class if you wish to have configurability for your
#      preprocessor.
#  
#      Any configurable traitlets this class exposed will be configurable in
#      profiles using c.SubClassName.attribute = value
#  
#      You can overwrite `preprocess_cell()` to apply a transformation
#      independently on each cell or `preprocess()` if you prefer your own
#      logic. See corresponding docstring for information.
#  
#      Disabled by default and can be enabled via the config by
#          'c.YourPreprocessorName.enabled = True'

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
#  Default: {'python': '# YOUR CODE HERE\nraise NotImplementedError()', 'R': '# YOUR CODE HERE\nfail()', 'matlab': "% YOUR CODE HERE\nerror('No Answer Given!')", 'octave': "% YOUR CODE HERE\nerror('No Answer Given!')", 'sas': '/* YOUR CODE HERE */\n %notImplemented;', 'java': '// YOUR CODE HERE'}
# c.ClearSolutions.code_stub = {'python': '# YOUR CODE HERE\nraise NotImplementedError()', 'R': '# YOUR CODE HERE\nfail()', 'matlab': "% YOUR CODE HERE\nerror('No Answer Given!')", 'octave': "% YOUR CODE HERE\nerror('No Answer Given!')", 'sas': '/* YOUR CODE HERE */\n %notImplemented;', 'java': '// YOUR CODE HERE'}

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

## Whether or not missing grade_cells should be added back to the notebooks being
#  graded.
#  Default: False
# c.OverwriteCells.add_missing_cells = False

## Whether to use this preprocessor when running nbgrader
#  See also: NbGraderPreprocessor.enabled
# c.OverwriteCells.enabled = True

## A text to add at the beginning of every missing cell re-added to the notebook
#  during autograding.
#  Default: 'This cell (id:{cell_id}) was missing from the submission. It was added back by nbgrader.\n\n'
# c.OverwriteCells.missing_cell_notification = 'This cell (id:{cell_id}) was missing from the submission. It was added back by nbgrader.\n\n'

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

## List of error names which won't stop the execution. Use this if the
#  ``allow_errors`` option it too general and you want to allow only specific
#  kinds of errors.
#  Default: []
# c.NotebookClient.allow_error_names = []

## If ``False`` (default), when a cell raises an error the execution is stopped
#  and a ``CellExecutionError`` is raised, except if the error name is in
#  ``allow_error_names``. If ``True``, execution errors are ignored and the
#  execution is continued until the end of the notebook. Output from exceptions
#  is included in the cell output in both cases.
#  Default: False
# c.NotebookClient.allow_errors = False

## An ordered list of preferred output type, the first encountered will usually
#  be used when converting discarding the others.
#  Default: ['text/html', 'application/pdf', 'text/latex', 'image/svg+xml', 'image/png', 'image/jpeg', 'text/markdown', 'text/plain']
# c.NotebookClient.display_data_priority = ['text/html', 'application/pdf', 'text/latex', 'image/svg+xml', 'image/png', 'image/jpeg', 'text/markdown', 'text/plain']

## If a cell execution was interrupted after a timeout, don't wait for the
#  execute_reply from the kernel (e.g. KeyboardInterrupt error). Instead, return
#  an execute_reply with the given error, which should be of the following form::
#  
#      {
#          'ename': str,  # Exception name, as a string
#          'evalue': str,  # Exception value, as a string
#          'traceback': list(str),  # traceback frames, as strings
#      }
#  Default: None
# c.NotebookClient.error_on_timeout = None

#  Default: []
# c.NotebookClient.extra_arguments = []

## If False (default), errors from executing the notebook can be allowed with a
#  ``raises-exception`` tag on a single cell, or the ``allow_errors`` or
#  ``allow_error_names`` configurable options for all cells. An allowed error
#  will be recorded in notebook output, and execution will continue. If an error
#  occurs when it is not explicitly allowed, a ``CellExecutionError`` will be
#  raised. If True, ``CellExecutionError`` will be raised for any error that
#  occurs while executing the notebook. This overrides the ``allow_errors`` and
#  ``allow_error_names`` options and the ``raises-exception`` cell tag.
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
#          The specific value ``:memory:`` (including the colon
#          at both end but not the back ticks), avoids creating a history file. Otherwise, IPython
#          will create a history file for each kernel.
#  
#          When running kernels simultaneously (e.g. via multiprocessing) saving history a single
#          SQLite file can result in database errors, so using ``:memory:`` is recommended in
#          non-interactive contexts.
#  Default: ':memory:'
# c.NotebookClient.ipython_hist_file = ':memory:'

## The kernel manager class to use.
#  Default: 'jupyter_client.manager.KernelManager'
# c.NotebookClient.kernel_manager_class = 'jupyter_client.manager.KernelManager'

## Name of kernel to use to execute the cells. If not set, use the kernel_spec
#  embedded in the notebook.
#  Default: ''
# c.NotebookClient.kernel_name = ''

## A callable which executes after a cell execution is complete. It is called
#  even when a cell results in a failure. Called with kwargs ``cell`` and
#  ``cell_index``.
#  Default: None
# c.NotebookClient.on_cell_complete = None

## A callable which executes when a cell execution results in an error. This is
#  executed even if errors are suppressed with ``cell_allows_errors``. Called
#  with kwargs ``cell`, ``cell_index`` and ``execute_reply``.
#  Default: None
# c.NotebookClient.on_cell_error = None

## A callable which executes just before a code cell is executed. Called with
#  kwargs ``cell`` and ``cell_index``.
#  Default: None
# c.NotebookClient.on_cell_execute = None

## A callable which executes just after a code cell is executed, whether or not
#  it results in an error. Called with kwargs ``cell``, ``cell_index`` and
#  ``execute_reply``.
#  Default: None
# c.NotebookClient.on_cell_executed = None

## A callable which executes before a cell is executed and before non-executing
#  cells are skipped. Called with kwargs ``cell`` and ``cell_index``.
#  Default: None
# c.NotebookClient.on_cell_start = None

## A callable which executes after the kernel is cleaned up. Called with kwargs
#  ``notebook``.
#  Default: None
# c.NotebookClient.on_notebook_complete = None

## A callable which executes when the notebook encounters an error. Called with
#  kwargs ``notebook``.
#  Default: None
# c.NotebookClient.on_notebook_error = None

## A callable which executes after the kernel manager and kernel client are
#  setup, and cells are about to execute. Called with kwargs ``notebook``.
#  Default: None
# c.NotebookClient.on_notebook_start = None

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

## Name of the cell tag to use to denote a cell that should be skipped.
#  Default: 'skip-execution'
# c.NotebookClient.skip_cells_with_tag = 'skip-execution'

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
#  setting ``timeout_func`` will cause the client to default to using the
#  ``timeout`` trait for all cells. The ``timeout_func`` trait overrides
#  ``timeout`` if it is not ``None``.
#  Default: None
# c.NotebookClient.timeout_func = None

#------------------------------------------------------------------------------
# ExecutePreprocessor(Preprocessor, NotebookClient) configuration
#------------------------------------------------------------------------------
## Executes all the cells in a notebook

## 
#  See also: NotebookClient.allow_error_names
# c.ExecutePreprocessor.allow_error_names = []

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

## 
#  See also: NotebookClient.error_on_timeout
# c.ExecutePreprocessor.error_on_timeout = None

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
# c.ExecutePreprocessor.kernel_manager_class = 'jupyter_client.manager.KernelManager'

## 
#  See also: NotebookClient.kernel_name
# c.ExecutePreprocessor.kernel_name = ''

## 
#  See also: NotebookClient.on_cell_complete
# c.ExecutePreprocessor.on_cell_complete = None

## 
#  See also: NotebookClient.on_cell_error
# c.ExecutePreprocessor.on_cell_error = None

## 
#  See also: NotebookClient.on_cell_execute
# c.ExecutePreprocessor.on_cell_execute = None

## 
#  See also: NotebookClient.on_cell_executed
# c.ExecutePreprocessor.on_cell_executed = None

## 
#  See also: NotebookClient.on_cell_start
# c.ExecutePreprocessor.on_cell_start = None

## 
#  See also: NotebookClient.on_notebook_complete
# c.ExecutePreprocessor.on_notebook_complete = None

## 
#  See also: NotebookClient.on_notebook_error
# c.ExecutePreprocessor.on_notebook_error = None

## 
#  See also: NotebookClient.on_notebook_start
# c.ExecutePreprocessor.on_notebook_start = None

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
#  See also: NotebookClient.skip_cells_with_tag
# c.ExecutePreprocessor.skip_cells_with_tag = 'skip-execution'

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
## 
#  See also: NotebookClient.allow_error_names
# c.Execute.allow_error_names = []

## Whether to use this preprocessor when running nbgrader
#  See also: NbGraderPreprocessor.enabled
# c.Execute.enabled = True

## If a cell execution was interrupted after a timeout, don't wait for the
#  execute_reply from the kernel (e.g. KeyboardInterrupt error). Instead, return
#  an execute_reply with the given error, which should be of the following form::
#  
#      {
#          'ename': str,  # Exception name, as a string
#          'evalue': str,  # Exception value, as a string
#          'traceback': list(str),  # traceback frames, as strings
#      }
#  Default: {'ename': 'CellTimeoutError', 'evalue': '', 'traceback': ['\x1b[0;31mCellTimeoutError\x1b[0m: No reply from kernel before timeout']}
# c.Execute.error_on_timeout = {'ename': 'CellTimeoutError', 'evalue': '', 'traceback': ['\x1b[0;31mCellTimeoutError\x1b[0m: No reply from kernel before timeout']}

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

## If execution of a cell times out, interrupt the kernel and continue executing
#  other cells rather than throwing an error and stopping.
#  Default: True
# c.Execute.interrupt_on_timeout = True

## 
#  See also: NotebookClient.iopub_timeout
# c.Execute.iopub_timeout = 4

## Path to file to use for SQLite history database for an IPython kernel.
#  See also: NotebookClient.ipython_hist_file
# c.Execute.ipython_hist_file = ':memory:'

## The kernel manager class to use.
#  See also: NotebookClient.kernel_manager_class
# c.Execute.kernel_manager_class = 'jupyter_client.manager.KernelManager'

## 
#  See also: NotebookClient.kernel_name
# c.Execute.kernel_name = ''

## 
#  See also: NotebookClient.on_cell_complete
# c.Execute.on_cell_complete = None

## 
#  See also: NotebookClient.on_cell_error
# c.Execute.on_cell_error = None

## 
#  See also: NotebookClient.on_cell_execute
# c.Execute.on_cell_execute = None

## 
#  See also: NotebookClient.on_cell_start
# c.Execute.on_cell_start = None

## 
#  See also: NotebookClient.on_notebook_complete
# c.Execute.on_notebook_complete = None

## 
#  See also: NotebookClient.on_notebook_error
# c.Execute.on_notebook_error = None

## 
#  See also: NotebookClient.on_notebook_start
# c.Execute.on_notebook_start = None

## If ``False`` (default), then the kernel will continue waiting for iopub
#  messages until it receives a kernel idle message, or until a timeout occurs,
#  at which point the currently executing cell will be skipped. If ``True``, then
#  an error will be raised after the first timeout. This option generally does
#  not need to be used, but may be useful in contexts where there is the
#  possibility of executing notebooks with memory-consuming infinite loops.
#  Default: True
# c.Execute.raise_on_iopub_timeout = True

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
#  See also: NotebookClient.skip_cells_with_tag
# c.Execute.skip_cells_with_tag = 'skip-execution'

## 
#  See also: NotebookClient.startup_timeout
# c.Execute.startup_timeout = 60

## 
#  See also: NotebookClient.store_widget_state
# c.Execute.store_widget_state = True

## The time to wait (in seconds) for output from executions. If a cell execution
#  takes longer, a TimeoutError is raised.
#  
#  ``None`` or ``-1`` will disable the timeout. If ``timeout_func`` is set, it
#  overrides ``timeout``.
#  Default: 30
# c.Execute.timeout = 30

## 
#  See also: NotebookClient.timeout_func
# c.Execute.timeout_func = None

#------------------------------------------------------------------------------
# InstantiateTests(NbGraderPreprocessor) configuration
#------------------------------------------------------------------------------
## The delimiter prior to snippets to be autotested
#  Default: 'AUTOTEST'
# c.InstantiateTests.autotest_delimiter = 'AUTOTEST'

## The filename where automatic testing code is stored
#  Default: 'autotests.yml'
# c.InstantiateTests.autotest_filename = 'autotests.yml'

## A dictionary mapping each Jupyter kernel's name to the comment string for that
#  kernel. For an example, one of the entries in this dictionary is "python" :
#  "#", because # is the comment character in python.
#  Default: {'ir': '#', 'python': '#', 'python3': '#'}
# c.InstantiateTests.comment_strs = {'ir': '#', 'python': '#', 'python3': '#'}

## Whether to use this preprocessor when running nbgrader
#  See also: NbGraderPreprocessor.enabled
# c.InstantiateTests.enabled = True

## Whether or not to complain if cells containing autotest delimiters are not
#  marked as grade cells. WARNING: disabling this will potentially cause things
#  to break if you are using the full nbgrader pipeline. ONLY disable this option
#  if you are only ever planning to use nbgrader assign.
#  Default: True
# c.InstantiateTests.enforce_metadata = True

## The delimiter prior to an autotest block if snippet results should be
#  protected by a hash function
#  Default: 'HASHED'
# c.InstantiateTests.hashed_delimiter = 'HASHED'

## A dictionary mapping each Jupyter kernel's name to the function that is used
#  to sanitize the output from the kernel within InstantiateTests.
#  Default: {'ir': <function InstantiateTests.<lambda> at 0x7f2d322d9f80>, 'python': <function InstantiateTests.<lambda> at 0x7f2d322da020>, 'python3': <function InstantiateTests.<lambda> at 0x7f2d322da0c0>}
# c.InstantiateTests.sanitizers = {'ir': <function InstantiateTests.<lambda> at 0x7f2d322d9f80>, 'python': <function InstantiateTests.<lambda> at 0x7f2d322da020>, 'python3': <function InstantiateTests.<lambda> at 0x7f2d322da0c0>}

## Whether to add a salt to digested answers
#  Default: True
# c.InstantiateTests.use_salt = True

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
## The delimiter marking the beginning of a marking scheme region
#  Default: 'BEGIN MARK SCHEME'
# c.ClearMarkScheme.begin_mark_scheme_delimeter = 'BEGIN MARK SCHEME'

## Whether or not to check if a marking scheme region contains an attachment, in
#  order to prevent leakage to student version of notebooks.
#  Default: True
# c.ClearMarkScheme.check_attachment_leakage = True

## Whether to use this preprocessor when running nbgrader
#  See also: NbGraderPreprocessor.enabled
# c.ClearMarkScheme.enabled = True

## The delimiter marking the end of a marking scheme region
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
#  Jupyter's root_dir.
#  Default: '.'
# c.Exchange.assignment_dir = '.'

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

## Collect the last submission before due date or the last submission if no
#  submission before due date.
#  Default: False
# c.ExchangeCollect.before_duedate = False

## Whether to cross-check the student_id with the UNIX-owner of the submitted
#  directory.
#  Default: True
# c.ExchangeCollect.check_owner = True

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

## Whether to replace missing files on fetch
#  Default: False
# c.ExchangeFetchAssignment.replace_missing_files = False

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

## Whether to replace missing files on fetch
#  See also: ExchangeFetchAssignment.replace_missing_files
# c.ExchangeFetch.replace_missing_files = False

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

## List assignments in submission cache.
#  Default: False
# c.ExchangeList.cached = False

## List inbound files rather than outbound.
#  Default: False
# c.ExchangeList.inbound = False

## Remove, rather than list files.
#  Default: False
# c.ExchangeList.remove = False

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

## Force overwrite existing files in the exchange.
#  Default: False
# c.ExchangeReleaseAssignment.force = False

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

## Force overwrite existing files in the exchange.
#  See also: ExchangeReleaseAssignment.force
# c.ExchangeRelease.force = False

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

## Format string for timestamps
#  See also: Exchange.timestamp_format
# c.ExchangeReleaseFeedback.timestamp_format = '%Y-%m-%d %H:%M:%S.%f %Z'

## Timezone for recording timestamps
#  See also: Exchange.timezone
# c.ExchangeReleaseFeedback.timezone = 'UTC'

#------------------------------------------------------------------------------
# ExchangeSubmit(Exchange) configuration
#------------------------------------------------------------------------------
## 
#  See also: Exchange.assignment_dir
# c.ExchangeSubmit.assignment_dir = '.'

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
#  Default: 'nbconvert.exporters.notebook.NotebookExporter'
# c.BaseConverter.exporter_class = 'nbconvert.exporters.notebook.NotebookExporter'

## Whether to overwrite existing assignments/submissions
#  Default: False
# c.BaseConverter.force = False

## Permissions to set on files output by nbgrader. The default is generally read-
#  only (444), with the exception of nbgrader generate_assignment and nbgrader
#  generate_feedback, in which case the user also has write permission.
#  Default: 0
# c.BaseConverter.permissions = 0

## An optional hook function that you can implement to do some work after
#  converting.  This function is called after the notebooks are converted and
#  should be used for specific converters such as Autograde, GenerateAssignment
#  or GenerateFeedback.
#  
#  It will be called as (all arguments are passed as keywords)::
#  
#      hook(assignment=assignment, student=student, notebooks=notebooks)
#  Default: None
# c.BaseConverter.post_convert_hook = None

## An optional hook function that you can implement to do some bootstrapping work
#  before converting.  This function is called before the notebooks are converted
#  and should be used for specific converters such as Autograde,
#  GenerateAssignment or GenerateFeedback.
#  
#  It will be called as (all arguments are passed as keywords)::
#  
#      hook(assignment=assignment, student=student, notebooks=notebooks)
#  Default: None
# c.BaseConverter.pre_convert_hook = None

#------------------------------------------------------------------------------
# GenerateAssignment(BaseConverter) configuration
#------------------------------------------------------------------------------
## Whether to create the assignment at runtime if it does not already exist.
#  Default: True
# c.GenerateAssignment.create_assignment = True

#  See also: BaseConverter.exporter_class
# c.GenerateAssignment.exporter_class = 'nbconvert.exporters.notebook.NotebookExporter'

## Whether to overwrite existing assignments/submissions
#  See also: BaseConverter.force
# c.GenerateAssignment.force = False

## Do not save information about the assignment into the database.
#  Default: False
# c.GenerateAssignment.no_database = False

## 
#  See also: BaseConverter.permissions
# c.GenerateAssignment.permissions = 0

## 
#  See also: BaseConverter.post_convert_hook
# c.GenerateAssignment.post_convert_hook = None

## 
#  See also: BaseConverter.pre_convert_hook
# c.GenerateAssignment.pre_convert_hook = None

#  Default: [<class 'nbgrader.preprocessors.headerfooter.IncludeHeaderFooter'>, <class 'nbgrader.preprocessors.instantiatetests.InstantiateTests'>, <class 'nbgrader.preprocessors.lockcells.LockCells'>, <class 'nbgrader.preprocessors.clearsolutions.ClearSolutions'>, <class 'nbgrader.preprocessors.clearoutput.ClearOutput'>, <class 'nbgrader.preprocessors.checkcellmetadata.CheckCellMetadata'>, <class 'nbgrader.preprocessors.computechecksums.ComputeChecksums'>, <class 'nbgrader.preprocessors.savecells.SaveCells'>, <class 'nbgrader.preprocessors.clearhiddentests.ClearHiddenTests'>, <class 'nbgrader.preprocessors.clearmarkingscheme.ClearMarkScheme'>, <class 'nbgrader.preprocessors.computechecksums.ComputeChecksums'>, <class 'nbgrader.preprocessors.checkcellmetadata.CheckCellMetadata'>]
# c.GenerateAssignment.preprocessors = [<class 'nbgrader.preprocessors.headerfooter.IncludeHeaderFooter'>, <class 'nbgrader.preprocessors.instantiatetests.InstantiateTests'>, <class 'nbgrader.preprocessors.lockcells.LockCells'>, <class 'nbgrader.preprocessors.clearsolutions.ClearSolutions'>, <class 'nbgrader.preprocessors.clearoutput.ClearOutput'>, <class 'nbgrader.preprocessors.checkcellmetadata.CheckCellMetadata'>, <class 'nbgrader.preprocessors.computechecksums.ComputeChecksums'>, <class 'nbgrader.preprocessors.savecells.SaveCells'>, <class 'nbgrader.preprocessors.clearhiddentests.ClearHiddenTests'>, <class 'nbgrader.preprocessors.clearmarkingscheme.ClearMarkScheme'>, <class 'nbgrader.preprocessors.computechecksums.ComputeChecksums'>, <class 'nbgrader.preprocessors.checkcellmetadata.CheckCellMetadata'>]

#------------------------------------------------------------------------------
# Assign(GenerateAssignment) configuration
#------------------------------------------------------------------------------
## 
#  See also: GenerateAssignment.create_assignment
# c.Assign.create_assignment = True

#  See also: BaseConverter.exporter_class
# c.Assign.exporter_class = 'nbconvert.exporters.notebook.NotebookExporter'

## Whether to overwrite existing assignments/submissions
#  See also: BaseConverter.force
# c.Assign.force = False

## 
#  See also: GenerateAssignment.no_database
# c.Assign.no_database = False

## 
#  See also: BaseConverter.permissions
# c.Assign.permissions = 0

## 
#  See also: BaseConverter.post_convert_hook
# c.Assign.post_convert_hook = None

## 
#  See also: BaseConverter.pre_convert_hook
# c.Assign.pre_convert_hook = None

#  See also: GenerateAssignment.preprocessors
# c.Assign.preprocessors = [<class 'nbgrader.preprocessors.headerfooter.IncludeHeaderFooter'>, <class 'nbgrader.preprocessors.instantiatetests.InstantiateTests'>, <class 'nbgrader.preprocessors.lockcells.LockCells'>, <class 'nbgrader.preprocessors.clearsolutions.ClearSolutions'>, <class 'nbgrader.preprocessors.clearoutput.ClearOutput'>, <class 'nbgrader.preprocessors.checkcellmetadata.CheckCellMetadata'>, <class 'nbgrader.preprocessors.computechecksums.ComputeChecksums'>, <class 'nbgrader.preprocessors.savecells.SaveCells'>, <class 'nbgrader.preprocessors.clearhiddentests.ClearHiddenTests'>, <class 'nbgrader.preprocessors.clearmarkingscheme.ClearMarkScheme'>, <class 'nbgrader.preprocessors.computechecksums.ComputeChecksums'>, <class 'nbgrader.preprocessors.checkcellmetadata.CheckCellMetadata'>]

#------------------------------------------------------------------------------
# Autograde(BaseConverter) configuration
#------------------------------------------------------------------------------
#  Default: [<class 'nbgrader.preprocessors.execute.Execute'>, <class 'nbconvert.preprocessors.clearmetadata.ClearMetadataPreprocessor'>, <class 'nbgrader.preprocessors.limitoutput.LimitOutput'>, <class 'nbgrader.preprocessors.saveautogrades.SaveAutoGrades'>, <class 'nbgrader.preprocessors.latesubmissions.AssignLatePenalties'>, <class 'nbgrader.preprocessors.checkcellmetadata.CheckCellMetadata'>]
# c.Autograde.autograde_preprocessors = [<class 'nbgrader.preprocessors.execute.Execute'>, <class 'nbconvert.preprocessors.clearmetadata.ClearMetadataPreprocessor'>, <class 'nbgrader.preprocessors.limitoutput.LimitOutput'>, <class 'nbgrader.preprocessors.saveautogrades.SaveAutoGrades'>, <class 'nbgrader.preprocessors.latesubmissions.AssignLatePenalties'>, <class 'nbgrader.preprocessors.checkcellmetadata.CheckCellMetadata'>]

## Whether to create the student at runtime if it does not already exist.
#  Default: True
# c.Autograde.create_student = True

## A dictionary with keys corresponding to assignment names and values being a
#  list of filenames (relative to the assignment's source directory) that should
#  NOT be overwritten with the source version. This is to allow students to e.g.
#  edit a python file and submit it alongside the notebooks in their assignment.
#  Default: {}
# c.Autograde.exclude_overwriting = {}

#  See also: BaseConverter.exporter_class
# c.Autograde.exporter_class = 'nbconvert.exporters.notebook.NotebookExporter'

## Whether to overwrite existing assignments/submissions
#  See also: BaseConverter.force
# c.Autograde.force = False

## 
#  See also: BaseConverter.permissions
# c.Autograde.permissions = 0

## 
#  See also: BaseConverter.post_convert_hook
# c.Autograde.post_convert_hook = None

## 
#  See also: BaseConverter.pre_convert_hook
# c.Autograde.pre_convert_hook = None

#  Default: [<class 'nbgrader.preprocessors.clearoutput.ClearOutput'>, <class 'nbgrader.preprocessors.deduplicateids.DeduplicateIds'>, <class 'nbgrader.preprocessors.overwritekernelspec.OverwriteKernelspec'>, <class 'nbgrader.preprocessors.overwritecells.OverwriteCells'>, <class 'nbgrader.preprocessors.checkcellmetadata.CheckCellMetadata'>]
# c.Autograde.sanitize_preprocessors = [<class 'nbgrader.preprocessors.clearoutput.ClearOutput'>, <class 'nbgrader.preprocessors.deduplicateids.DeduplicateIds'>, <class 'nbgrader.preprocessors.overwritekernelspec.OverwriteKernelspec'>, <class 'nbgrader.preprocessors.overwritecells.OverwriteCells'>, <class 'nbgrader.preprocessors.checkcellmetadata.CheckCellMetadata'>]

#------------------------------------------------------------------------------
# GenerateFeedback(BaseConverter) configuration
#------------------------------------------------------------------------------
#  See also: BaseConverter.exporter_class
# c.GenerateFeedback.exporter_class = 'nbconvert.exporters.notebook.NotebookExporter'

## Whether to overwrite existing assignments/submissions
#  See also: BaseConverter.force
# c.GenerateFeedback.force = False

## 
#  See also: BaseConverter.permissions
# c.GenerateFeedback.permissions = 0

## 
#  See also: BaseConverter.post_convert_hook
# c.GenerateFeedback.post_convert_hook = None

## 
#  See also: BaseConverter.pre_convert_hook
# c.GenerateFeedback.pre_convert_hook = None

#  Default: [<class 'nbgrader.preprocessors.getgrades.GetGrades'>, <class 'nbconvert.preprocessors.csshtmlheader.CSSHTMLHeaderPreprocessor'>]
# c.GenerateFeedback.preprocessors = [<class 'nbgrader.preprocessors.getgrades.GetGrades'>, <class 'nbconvert.preprocessors.csshtmlheader.CSSHTMLHeaderPreprocessor'>]

#------------------------------------------------------------------------------
# Feedback(GenerateFeedback) configuration
#------------------------------------------------------------------------------
#  See also: BaseConverter.exporter_class
# c.Feedback.exporter_class = 'nbconvert.exporters.notebook.NotebookExporter'

## Whether to overwrite existing assignments/submissions
#  See also: BaseConverter.force
# c.Feedback.force = False

## 
#  See also: BaseConverter.permissions
# c.Feedback.permissions = 0

## 
#  See also: BaseConverter.post_convert_hook
# c.Feedback.post_convert_hook = None

## 
#  See also: BaseConverter.pre_convert_hook
# c.Feedback.pre_convert_hook = None

#  See also: GenerateFeedback.preprocessors
# c.Feedback.preprocessors = [<class 'nbgrader.preprocessors.getgrades.GetGrades'>, <class 'nbconvert.preprocessors.csshtmlheader.CSSHTMLHeaderPreprocessor'>]

#------------------------------------------------------------------------------
# GenerateSolution(BaseConverter) configuration
#------------------------------------------------------------------------------
## Whether to create the assignment at runtime if it does not already exist.
#  Default: True
# c.GenerateSolution.create_assignment = True

#  See also: BaseConverter.exporter_class
# c.GenerateSolution.exporter_class = 'nbconvert.exporters.notebook.NotebookExporter'

## Whether to overwrite existing assignments/submissions
#  See also: BaseConverter.force
# c.GenerateSolution.force = False

## 
#  See also: BaseConverter.permissions
# c.GenerateSolution.permissions = 0

## 
#  See also: BaseConverter.post_convert_hook
# c.GenerateSolution.post_convert_hook = None

## 
#  See also: BaseConverter.pre_convert_hook
# c.GenerateSolution.pre_convert_hook = None

#  Default: [<class 'nbgrader.preprocessors.headerfooter.IncludeHeaderFooter'>, <class 'nbgrader.preprocessors.lockcells.LockCells'>, <class 'nbgrader.preprocessors.clearoutput.ClearOutput'>, <class 'nbgrader.preprocessors.clearmarkingscheme.ClearMarkScheme'>, <class 'nbgrader.preprocessors.execute.Execute'>]
# c.GenerateSolution.preprocessors = [<class 'nbgrader.preprocessors.headerfooter.IncludeHeaderFooter'>, <class 'nbgrader.preprocessors.lockcells.LockCells'>, <class 'nbgrader.preprocessors.clearoutput.ClearOutput'>, <class 'nbgrader.preprocessors.clearmarkingscheme.ClearMarkScheme'>, <class 'nbgrader.preprocessors.execute.Execute'>]

#------------------------------------------------------------------------------
# GenerateSourceWithTests(BaseConverter) configuration
#------------------------------------------------------------------------------
#  See also: BaseConverter.exporter_class
# c.GenerateSourceWithTests.exporter_class = 'nbconvert.exporters.notebook.NotebookExporter'

## Whether to overwrite existing assignments/submissions
#  See also: BaseConverter.force
# c.GenerateSourceWithTests.force = False

## 
#  See also: BaseConverter.permissions
# c.GenerateSourceWithTests.permissions = 0

## 
#  See also: BaseConverter.post_convert_hook
# c.GenerateSourceWithTests.post_convert_hook = None

## 
#  See also: BaseConverter.pre_convert_hook
# c.GenerateSourceWithTests.pre_convert_hook = None

#  Default: [<class 'nbgrader.preprocessors.instantiatetests.InstantiateTests'>, <class 'nbgrader.preprocessors.clearoutput.ClearOutput'>, <class 'nbgrader.preprocessors.checkcellmetadata.CheckCellMetadata'>]
# c.GenerateSourceWithTests.preprocessors = [<class 'nbgrader.preprocessors.instantiatetests.InstantiateTests'>, <class 'nbgrader.preprocessors.clearoutput.ClearOutput'>, <class 'nbgrader.preprocessors.checkcellmetadata.CheckCellMetadata'>]
