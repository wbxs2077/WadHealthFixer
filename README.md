[中文](https://raw.githubusercontent.com/wbxs2077/WadHealthFixer/main/README_CN.md) | [English](https://github.com/wbxs2077/WadHealthFixer/blob/main/README.md)
## Wad Health Fixer

Wad Health Fixer is a tool designed to fix the issue of disappearing health bars in the League of Legends game caused by corrupted wad.client files. It automates the process of repairing these files to ensure a smooth gaming experience for players.

### Dependencies

This project depends on the following:

- [ritobin](https://github.com/moonshadow565/ritobin): A tool for manipulating League of Legends binary files.
- [cs-lol](https://github.com/LeagueToolkit/cslol-manager): A package containing various tools for League of Legends, including the necessary resources for handling wad.client files.
- [CommunityDragon/Data](https://github.com/CommunityDragon/Data): Provides essential data files, including hashes, required for the operation of the tool.

### Compilation

The project is compiled and packaged into an executable (exe) file using Nuitka, ensuring easy deployment and usage on Windows platforms.

### Usage

1. Clone this repository to your local machine.
2. Install the required dependencies: ritobin and cs-lol.
3. Download the necessary data files from CommunityDragon/Data.
4. Run the script `wad_health_fixer.py`.
5. Enter the path to the folder containing the wad.client files you want to fix.
6. Follow the on-screen instructions to complete the process.

### License

This project is licensed under the [MIT License](LICENSE).

### Contributions

Contributions are welcome! If you encounter any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.

### Acknowledgments

Special thanks to the developers of ritobin, cs-lol, and CommunityDragon/Data for their valuable contributions to the League of Legends community.
