# PyNDI
 
A very simple Python wrapper for NewTek NDI using CFFI (must be added as a dependency) created by [CarlosFdez](https://github.com/CarlosFdez)
and extended by [quidquid](https://github.com/quidquid) and [labrat97](https://github.com/labrat97).
Has basic functionality for both receiving and sending video, but not all options are implemented. Use at your own risk.

Tested with NewTek NDI 4.5 and Python 3.8, on Windows, Mac, and Linux. 

The NDI runtime must be installed. Recommended NDI tools to be installed too for testing. 

### Demos

`SimpleSourceViewer` is just that. Pick an existing NDI source and display it.

`SimpleSender` creates an NDI source using either the webcam or a generated color-cycling image.


### Known Issues
| Issues                                                            | Resolution                                                  | 
| ----------------------------------------------------------------- | ----------------------------------------------------------- |
| Sometimes when retrieving sources, not all sources are found.     | Refreshing the list of sources normally fixes this problem. | 



