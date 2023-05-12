![Alt text](https://github.com/EBSP-Indexer/EBSP-Indexer/blob/dev/resources/ebsd_gui.png?raw=true "Electron backscatter pattern Indexer")
[![GitHub release](https://img.shields.io/github/release/EBSP-Indexer/EBSP-Indexer.svg)](https://GitHub.com/EBSP-Indexer/EBSP-Indexer/releases/)
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.7925262.svg)](https://doi.org/10.5281/zenodo.7925262)
[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) 

[![macOS](https://svgshare.com/i/ZjP.svg)](https://svgshare.com/i/ZjP.svg)
[![Windows](https://svgshare.com/i/ZhY.svg)](https://svgshare.com/i/ZhY.svg)
<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/badge/all_contributors-3-orange.svg?style=flat-square)](#contributors-)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

EBSP Indexer is a graphical user interface that allows for processing and indexing of Electron backscatter patterns, generated by scanning electron microscopes. Its goal is to make the rich functionality of the open source library [kikuchipy](https://zenodo.org/record/7808659) more accessible to users, without requireing knowledge of python or the library itself.

The GUI supports:
- Customizable Dictionary and Hough indexing
- Refinement of orinetations
- Signal improvements
    - Static background removal
    - Dynamic background removal
    - Averaging by neighbour patterns
- Pattern center calibration from
    - Existing calibration patterns
    - Selection of patterns
    - Working distance for added Microscopes
- Region of interest
- Signal navigation of patterns
- Pre- and post-indexing maps
- Accessible interactive interpreter for python

The project was originally developed by students at [The Department of Material Science](https://www.ntnu.edu/ima/research/emlab) at [Norwegian University of Science and Techonolgy (NTNU)](https://www.ntnu.edu/), and is open source and free to use.

## Known issues :heavy_exclamation_mark: 
- Refinement of orientations of a crystal map which includes not_indexed points,
  might produce results that cannot be opened in signal navigation.
- Updating the application's settings will set the current working directory to 
  the specified default directory (if checked).
- Updating the application's settings will reset the current selected file, 
  even though it appears to be selected.
- When saving a merged crystal map in the case where only one phase is identified, 
  save will fail since a crystal map with the same name exists already.

## Minimum requirements 🔧
- Windows 10/11 **or** macOS 13 (Ventura)
- x86_64-based CPU (arm64 chipset is experimental)

In addition, the windows version requires [Microsoft Visual C++ Redistributable packages for Visual Studio 2015, 2017, 2019, and 2022.](https://learn.microsoft.com/en-US/cpp/windows/latest-supported-vc-redist?view=msvc-170) This is included in our installer, and is automatically installed if needed.

## Downloads ⬇️
Installer for Windows and App for macOS are available to download from [Zenodo](https://zenodo.org/record/7925262) or [SourceForge](https://sourceforge.net/projects/ebsp-indexer/).

## Contributors ✨

Thanks goes to these wonderful people ([emoji key](https://allcontributors.org/docs/en/emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Erlendos12"><img src="https://avatars.githubusercontent.com/u/99336047?v=4?s=100" width="100px;" alt="Erlend M. Østvold"/><br /><sub><b>Erlend M. Østvold</b></sub></a><br /><a href="https://github.com/EBSP-Indexer/EBSP-Indexer/commits?author=Erlendos12" title="Code">💻</a> <a href="https://github.com/EBSP-Indexer/EBSP-Indexer/issues?q=author%3AErlendos12" title="Bug reports">🐛</a> <a href="https://github.com/EBSP-Indexer/EBSP-Indexer/commits?author=Erlendos12" title="Documentation">📖</a> <a href="#ideas-Erlendos12" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/olavlet"><img src="https://avatars.githubusercontent.com/u/113110330?v=4?s=100" width="100px;" alt="olavlet"/><br /><sub><b>olavlet</b></sub></a><br /><a href="https://github.com/EBSP-Indexer/EBSP-Indexer/commits?author=olavlet" title="Code">💻</a> <a href="https://github.com/EBSP-Indexer/EBSP-Indexer/issues?q=author%3Aolavlet" title="Bug reports">🐛</a> <a href="https://github.com/EBSP-Indexer/EBSP-Indexer/commits?author=olavlet" title="Documentation">📖</a> <a href="#ideas-olavlet" title="Ideas, Planning, & Feedback">🤔</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/htrellin"><img src="https://avatars.githubusercontent.com/u/80631936?v=4?s=100" width="100px;" alt="htrellin"/><br /><sub><b>htrellin</b></sub></a><br /><a href="https://github.com/EBSP-Indexer/EBSP-Indexer/commits?author=htrellin" title="Code">💻</a> <a href="https://github.com/EBSP-Indexer/EBSP-Indexer/issues?q=author%3Ahtrellin" title="Bug reports">🐛</a> <a href="https://github.com/EBSP-Indexer/EBSP-Indexer/commits?author=htrellin" title="Documentation">📖</a> <a href="#ideas-htrellin" title="Ideas, Planning, & Feedback">🤔</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/all-contributors/all-contributors) specification. Contributions of any kind welcome!
