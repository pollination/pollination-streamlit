import streamlit as st

from .api.client import ApiClient
from .interactors import Job, Run


@st.cache
def api_key_input() -> str:
    return st.text_input(label='API Key', type='password')


@st.cache(allow_output_mutation=True)
def _get_job(job_id, project, owner, api_key=None) -> Job:
    client = ApiClient(api_token=api_key)
    return Job(owner, project, job_id, client)


@st.cache(allow_output_mutation=True)
def _get_run(job_id, project, owner, run_id, api_key=None) -> Job:
    client = ApiClient(api_token=api_key)
    return Run(owner, project, job_id, run_id, client)


def job_selector(api_key: str = None, label: str = 'Job URL', default: str = None,
        help: str = None
    ) -> Job:
    job_url = st.text_input(label=label, value=default, help=help)
    if not job_url or job_url == 'None':
        return None

    url_split = job_url.split('/')
    job_id = url_split[-1]
    project = url_split[-3]
    owner = url_split[-4]

    return _get_job(job_id, project, owner, api_key)


def run_selector(
        api_key: str = None, label: str = 'Run URL', default: str = None,
        help: str = None
    ) -> Run:
    run_url = st.text_input(label=label, value=default, help=help)
    if not run_url or run_url == 'None':
        return None

    url_split = run_url.split('/')
    run_id = url_split[-1]
    job_id = url_split[-3]
    project = url_split[-5]
    owner = url_split[-6]

    return _get_run(job_id, project, owner, run_id, api_key)
