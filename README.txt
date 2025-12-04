####### ATTRIBUTION

If you have made use of this data in your project/paper, please cite our paper: "Speech Recognition and Multi-Speaker Diarization of Long Conversations".

(APA style)
Mao, H. H., Li, S., McAuley, J., & Cottrell, G. (2020). Speech Recognition and Multi-Speaker Diarization of Long Conversations. INTERSPEECH.

(BibTex)
@inproceedings{interspeech_2020_multispk_asr_sd,
  author    = {Huanru Henry Mao and
               Shuyang Li and
               Julian J. McAuley and
               Garrison W. Cottrell},
  title     = {Speech Recognition and Multi-Speaker Diarization of Long Conversations},
  booktitle = {Interspeech 2020, 21st Annual Conference of the International Speech
               Communication Association, Shanghai, China, 25-29 October 2020},
  year      = {2020},
  url       = {https://arxiv.org/abs/2005.08072},
}

####### TRANSCRIPTS

Transcripts comprise three files:
    test-transcripts-aligned.json (Test split conversations)
    train-transcripts-aligned.json (Train split conversations)
    valid-transcripts-aligned.json (Validation/dev split conversations)

These files, when loaded via `json.load(open(f, 'r+'))`, are each a dictionary with the following structure:

{ <Dictionary of episodes>
    Episode ID (str) :
        [ <List of turns>
            { <Dictionary representing a turn>
                'episode': (str) Episode ID e.g. ep-11,
                'act': (str) Act of the podcast this turn belongs to,
                'act_title': (str) Title of the act,
                'role': (str) Speaker role e.g. host/interviewer/subject,
                'speaker': (str) Speaker name,
                'utterance_start': (float) Offset of start of utterance in seconds,
                'utterance_end': (float) Offset of end of utterance in seconds,
                'utterance': (str) Utterance text,
                'n_sentences': (int) Number of sentences in utterance, tokenized via nltk.tokenize.sent_tokenize,
                'n_words': (int) Number of words in utterance, tokenized via nltk.word_tokenize,
                'alignments': [ <List of forced alignments for utterance words>
                    [ <Tuple of begin/end/word #>
                        (float) Offset of word start from beginning of episode,
                        (float) Offset of word end from beginning of episode,
                        (int) Word order in the utterance,
                    ],
                    ...
                ],
                'has_q': (bool) Whether the utterance contains a question,
                'end_q': (bool) Whether the utterance ends in a question
            },
            ...
        ],
    ...
}

This release also includes a speaker map to replicate our speaker indices at `full-speaker-map.json`, comprising a single dictionary of <speaker name> : <speaker ID>.

####### AUDIO

Audio files are copyrighted by This American Life, and as such we are not distributing these alongside the annotated transcripts.
We have included a file, `download_page_snapshot.html`, that contains the download links from which we obtained the raw MP3 audio.

If you have tried to download the files and are experiencing difficulties in training our model or replicating our results, please reach out to shl008@eng.ucsd.edu for help.


###### CODE

Code will be released at: https://github.com/calclavia/tal-asrd


####### DISCLAIMERS

All data is distributed exclusively for the purpose of non-commercial, research usage.
Relevant copyrights and trademarks of podcast audio and content belong to This American Life (https://www.thisamericanlife.org/).
Annotations copyright Shuyang Li & Henry Mao 2020.
