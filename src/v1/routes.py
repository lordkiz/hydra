#!flask/bin/python
import requests as python_request
from flask import Blueprint, abort, request, jsonify
from keybert import KeyBERT
from bs4 import BeautifulSoup

bp = Blueprint('v1', __name__)

kw_model = KeyBERT()

@bp.route('/')
def index():
  return "V1 Home"

@bp.route('/text/extract-keywords', methods=['POST'])
def extract_keywords_from_text():
  if not request.json or not 'text' in request.json:
    abort(400)
  text = request.json['text']
  keywords = kw_model.extract_keywords(text)
  return jsonify({ 'data': keywords})

@bp.route('/html/extract-keywords', methods=['POST'])
def extract_keywords_from_html():
  if not request.json or not 'url' in request.json:
    abort(400)
  url = request.json['url']
  resp = python_request.get(url)
  if resp.status_code == 200:
    soup = BeautifulSoup(resp.content, 'html.parser')
    text = soup.text
    keywords = kw_model.extract_keywords(text, keyphrase_ngram_range=(3, 3), stop_words='english', top_n=20)
    return jsonify({ 'data': keywords })
