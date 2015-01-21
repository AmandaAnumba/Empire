from flask import Flask, Blueprint, render_template, request, redirect, escape, jsonify, abort
from jinja2 import TemplateNotFound

dashboard = Blueprint('dashboard', __name__)
