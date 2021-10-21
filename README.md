# Binary Search Tree Project

![GitHub last commit](https://img.shields.io/github/last-commit/1danielsc/BinarySearchTree)  ![GitHub issues](https://img.shields.io/github/issues-raw/1danielsc/BinarySearchTree)


> Status: Developing ⚠️
>
>Technology used: Python

## Table of Contents

  - [Description](#1-description)
  - [Installation](#2-installation)
  - [Code details](#3-code-details)
  - [How to run it](#4-how-to-run-it)
  - [Roadmap](#5-roadmap)


## 1. Description

This project is an implementation of Binary Search Tree data structure in Python. 


This application is set to receive an input file consisting of sequential instructions to be executed. The instructions supported can be found at [Files](#33-files).


## 2. Installation
You should have [Python 3.10.0](https://www.python.org/downloads/release/python-3100/) version installed on your computer.


## 3. Code details

All details about the code and its implementation:

  - [Classes](#31-classes)
  - [Methods](#32-methods)
  - [Files](#33-files)

### 3.1 Classes

#### 3.1.1 Node

The element to be stored in a tree.

#### 3.1.1.1 Attributes

- self.key - Integer number
- self.left - Reference to the left subtree
- self.right - Reference to the right subtree


#### 3.1.1 Binary Tree

This is the class which most of elementary methods of a Binary Tree is implemented.

#### 3.1.1.1 Attributes


- self.root - Reference to the node element that is the root of the tree


#### 3.1.2 Binary Search Tree

### 3.2 Methods



### 3.3 Files

#### 3.3.1 instructions.txt

All operations have to be written sequentially on this file.

The program will read each instruction at a time and execute it.

Operations suported:
- Insert [element]
- Delete [element]
- Search [element]
- Print
- FindKthElement [element]
- Size

Proper way to write on file: 
>instruction + " " + element

Instruction in CAPS followed by a white space and a number right after it if necessary.

Examples:

PRINT

INSERT 20



## 4. How to run it

This section will contain all the necessary information to run this application.

## 5. Roadmap

Features to be added to this project in the future:

- AVL Tree
- Support to read an input file consisting of ordered operations that the program must follow
- More methods. For instance: median(), mean() and isBinarySearchTree().
- Dedicated class to run the program