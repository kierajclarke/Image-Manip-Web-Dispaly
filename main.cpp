#include <fstream>
#include <iostream>
using namespace std;
#include <filesystem>

const string python = "python";

string get_filename();
void print_menu();
char get_manip_choice();

int main() {
    cout << "Welcome to the image manipulator!" << endl;
    string filename = get_filename();
    cout << "Using file " << filename << "." << endl;
    print_menu();
    char choice = get_manip_choice();
    cout << "Processing. Go to Python program when it opens. May take a few seconds." << endl;
    string command;
    switch (choice) {
        // Use command-line arguments to pass the filename and manip to the Python file
        case 'a': command = python + " ../render.py " + filename + " flip";
            break;
        case 'b': command = python + " ../render.py " + filename + " mirror";
            break;
        case 'c': command = python + " ../render.py " + filename + " invert";
            break;
        case 'd': exit(0);
    }
    system(command.c_str());
    return 0;
}


string get_filename() {
    string filename = "frosted-rose.jpg";
    return filename;
}

void print_menu() {
    cout << "Main Menu: (a) flip, (b) mirror, (c) invert, (d) exit" << endl;
}

char get_manip_choice() {
    char option;
    cout << "Enter your choice (a, b, c, or d): " << endl;
    cin >> option;

    while (option != 'a' && option != 'b' && option != 'c' && option != 'd') {

        cout << "Invalid choice. Enter (a, b, c, or d): " << endl;
        cin >> option;
    }


    return option;
}