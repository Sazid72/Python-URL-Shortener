# Python URL Shortener

A simple command-line URL shortener built with Python using the `pyshorteners` library. The program takes a long URL from the user and generates a shortened TinyURL link while handling common errors gracefully.

## Features

* Shortens long URLs using TinyURL
* Handles invalid URLs
* Handles API response failures
* Uses exception handling for robust error management
* Simple command-line interface

---

## Project Description

### What I Made

I built a command-line URL shortener in Python that allows users to enter a URL and receive a shortened version using the TinyURL service. The application uses the `pyshorteners` library to communicate with the TinyURL API and includes exception handling to provide meaningful error messages when something goes wrong.

### Why I Made It

I created this project to practice working with third-party Python libraries, exception handling, and writing clean, modular code. I also wanted to learn how Python programs can interact with online services through APIs.

### How I Made It

The project was built using Python and the `pyshorteners` library.

The program is divided into two functions:

* `main()` collects the user's input and displays the result.
* `short_url()` handles the URL shortening process and catches possible exceptions.

I used Python's `try` and `except` statements to handle different errors such as invalid URLs, API failures, and unexpected exceptions.

### Challenges I Faced

One of the challenges was understanding which exceptions could be raised by the `pyshorteners` library and how to handle them properly. I also considered adding my own URL validation, but after exploring the library's behavior, I learned that it already validates URLs internally and raises appropriate exceptions. This helped keep the code simpler and avoided unnecessary duplicate validation.

---

## Technologies Used

* Python 3
* pyshorteners

---

## Installation

Clone the repository:

```bash
git clone https://github.com/your-username/url-shortener.git
cd url-shortener
```

Install the required package:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the program:

```bash
python main.py
```

Example:

```text
Enter your URL: https://www.python.org/

https://tinyurl.com/xxxxxxxx
```

---

## Project Structure

```text
url-shortener/
├── main.py
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Future Improvements

* Support multiple URL shortening services
* Add clipboard support
* Build a GUI version with Tkinter or CustomTkinter
* Create a web version using Flask or FastAPI
* Store previously shortened URLs in a database

---

## License

This project is open source and available under the MIT License.

## Author
Md. Sazid Al Mafi

