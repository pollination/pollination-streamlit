from pollination_streamlit.authentication import _decrypt_cookie


def test_decrypt():
    cookie = "MTY0NzUyMTM2M3xjM1Z3WlhJdGMyVmpjbVYwTFhaaGJIVmx8Zq5Ks3q90QdgL5znATZfz5LsGWUcSc5CGIOeZn-EQBE="
    value = "super-secret-value"
    assert _decrypt_cookie(cookie) == value


def test_failing_decrypt():
    """This is a sample cookie that used to fail to decrypt."""
    cookie = 'MTY3ODM5NzQzNXxaWGxLYUdKSFkybFBhVXBUVlhwSk1VNXBTWE5KYlhSd1drTkpOa2xxVlRSUFJFa3dXVlJKTWxwcVJteFpNbEV4VG1wRmVVNHlWVFJQVjFreFdYcHJkMWxVWnpSTlJGbDRUVlJLYUZsdFZUVlBWMDFwVEVOS01HVllRV2xQYVVwTFZqRlJhV1pSTG1WNVNuVlpWekZzU1dwdmFWUlhPWHBrUjBaM1lVZEZaMVV5Um10YVYyUnZZVmhDZG1SWVNXZFZiVGt4V2toT2FHTnRhMmxNUTBwM1lWZE9NR1JZU214SmFtOXBZVWhTTUdOSVRUWk1lVGx6WVVSTmRWb3lPWFphTW5oc1pGaE9iR050VG5aaWJsSnNZbTVSZFZreU9YUk1Na1YwVERCR1VHRkVSVEJTTW1STFRYcGpNMlZwTVZSVlZUZ3lVVzFzYzJWV1JtRk5iWEJVWVZoa1FsZEdTbE5STTFwd1dteG9iMUZ0YUV0VE1VWlBXWHBHZEZKVVZYaFdia0l5VGpOa1JXRlVSbE5VYXpGdlpESkdabFpGVG5CVVNHaHBWVVZrYmxwcWFISlNWV2d3VmpOcmVsZFdXbWxWVm5CWlZWZHplVlpGWkhGVlIxb3hXVEZOZVdNd1NrcGFiR1JKVWtaU2RHSlVVblJpVlVrelRUSjRXVTVJWkdoaFZUa3hXSHBDYWxSR1NucFNWbEp4Vkd0c2QxTkZhekpXYldRd1dUSlNWMVJzUmpGTlZYaHFZMnR3VVZKNlNYUlVNV1JzV1cxMFYwNUZXbXBhTTI5NVRXdGtWR05WTlRCVGExRjZaVlprVTJWVldtbGFXRXBOVWxod1lXSlhOWE5pVmtKNlZtMUdXR1ZJWkdsTk0xWTBZVlZHYW1WR1FrZFZNMG95VEZka2FtTllSWHBsYkdReldqRmpNazE2VmtkV01WWllWMjFvU1U5SFZrNWlXRlpaVjJ0R01WcEdaREJaTUVaTlZWaGFhR0pyYkZKWFNHeDFUbTAxTUZsdWNESldha1pQVFZkYWQxcFhkRnBhTUZKTFZraHdjazVFVVRWaFIxSkVWRzA1VDFWSVkzbFhSMmhQV1ZWU1IySlhlREZPTVVaWVQwVktWRmxUTVU1TVdHc3lUVEZyTUZneVVqTlZWemwyVmtWR1ZVMVZhRUpTVjFKNVVXMW9UVTVVUlhwT2JXaFlWVWN4VW1Oc09EQlNiRUpSWTFoS1dtVlhVbnBpTTAxNlpGVmpNRTB3VG5GWWVURXhaVmRPYkdGNlozaFdWamgzVEZoc2IxSkhSbEpaTVVwRlYxVmpNbEV6V21GU1YxSTFXVmRTZVdGcVpFSmhhMFV5VldwYWQxb3dhREpOUlZKcVZEQTFOazFWZDNobFJVcHlUakp3YTFKdVpHMWFWMnQ2VG10d01GTXhUa0pVTVZKdFdXNWtlbEpzT1hKT01FNXVWMVV4UW1Fd1RYbFpla3B5VFROR2MxWnNjRXRrVmtwb1pFaG9abFF5VVROaFJtd3pUVEpPUTB4VlVuZE9TSEJOV0ROS05GUllUbWhsVkUwelRrZFpkRlpxYkhsVVZuQkNZMWhqZDFaSGVFNU5hMk0xWkcxS1JrMVlXak5VUm1od1kyMUdhbHBGWkVkVVZYUnVVbXBhYjFRd1pGaGpiRnBaVTFSa2VVOUhOWHBUUm1SVlkwUmtNMU15VmxoVFdGRjRZVEJHVFZZeU5VSlBTRlpXVW5wa1ExUnFaREprTVd4bVpGZGtUbVZJWkZOT1ZGcEdZMVJDZEUwemFFaFhSMmd5WlZod1NGSnVjRWRVYlRoNlYwYzFXV1ZyVWpGVVdGWnVZVU14Ymxrd1ZrSlNNRTVJVG1wYVNsUnFUbFpWUjFKNVVrVTVWRTlZUlhSamFrNVBURmRTVWt4VWFHWlhXR3g1V1d4T2JGb3dlSFZPU0UwMVZsVlNiV0pWT0RGaVZ6QTFWMVJzYTFGVVVYUlNWbHA2Vm0xa1RWSnVaSEZsUlRWV1lXdGFhR1ZyY0Zsa1IxWm1VbFZvVDJWcVNtdGpiVm93V0ROd2JGcHRXbXBoTTFKWVVtMXNjR05zV2tOaldIQnZZMWN4YWxOWWJFcE9Sa28wV201T1JWUkdaR2hYYlhSS1UwaHNTazlWY0c5bFdFcFFXWHBTTVU1cmFIUlBWbHBQVEZVNVMxVkdaRmhhUlUwMVkxWlNNbFpWVGtkUFZUbFlWVmhXTmxkRlJUbGplbXN5VEZkTmFVeERTbWhaTWs1MlpGYzFNRWxxYjJsYVYwVjVUVVJHYWxsVVkzUlplbU0wVFhrd01GbHFRWHBNVjBacFdsUk5kRTR5UlhoWlZFMTZXVmRPYlZsVVp6QkphWGRwWVZoT2VrbHFiMmxoU0ZJd1kwaE5Oa3g1T1hwYVYwNHhZMjFXTUdJeWRHeGlhVFZ1WWpJNWJtSkhWWFZaTWpsMFRETkNkbUpIZUhCaWJVWXdZVmM1ZFV4WVRqQlpWMlJ3WW0xamRFMVhVVEpaVkdkcFRFTkthR1JYVVdsUGFVcDNZako0YzJGWE5XaGtSMngyWW1reGVtUkhSbTVoVnpWdVRGUkdhMDV0UlRSSmFYZHBXVmhXTUdGR09UQmhWekZzU1dwdmVFNXFXWGxOVkVVeVQxUlZORXhEU2pGak1sWjVXREpzYTBscWIybFVNRzk1VkZkc1NtRXpUVE5VTVZaR1VWVmFXVkpFUmt0aFdHd3pWakF4VDFaSWJIVk5VMGx6U1c1T01WbHBTVFpKYXpsTFRXc3hjRk5YZEhwT01EbFdVbFZHUjFkRlVYaFRiV3cxWkRGa1RsUnNValZpYWtWcFRFTktjRmxZVVdsUGFrVXlUbnBuZWs5VVl6Qk5SR056U1cxV05HTkRTVFpOVkZrelQwUlJkMDFVUVhkT2VYZHBXbGN4YUdGWGQybFBhVXAwWWpOT01GbFlRbTlaVlVKeldWZFNOVmx1Vm01TWJsSjJZako0ZWtscGQybGFWekZvWVZkNFptUnRWbmxoVjFwd1dsZFJhVTl1VW5sa1YxVnpTVzFhY0dOdFZtbFpXRTVzU1dwd04wbHRiR3RhVnpVd1lWaFNjRnBZVFdsUGJuTnBXakk1ZGxveWVHeE1iVTUyWWxOSk5sZDVTWGhOVkVrMVQwUk5NVTFFV1ROT2FtZDNUbXBGTVU1NldUSlBSR3RwV0ZOM2FWcFhNV2hoVjNkcFQyeHphV0pYT1hwa1IwWjNZVWRHUVdKSFJtdGxWMG94V25rMU1HSXlPWE5qZVVwa1psTjNhV015Ykc1aWJEbHdZbXc1ZDJOdE9USmhWMUpzWTJsSk5rbHRaSFppTW1SeldsTTFhbUl5TUdsbVdEQXVaREpqTnpaa1MxRlBZVmhPYjNKTk5ERk1aMEZxY0RGR05WaG9SR3RZZEhwcVlYQTFabHA0T0dWNGVERlFNSFpKTFUxclUzVndlamxrT1RaSE4yWnRlbVp2YUZSM1FrVm5Rbms1Y3pGQk9URnZPRFZTWDNkNlVUZGxlRFJmV1ZSemJFOUhXSHBaTTJaNVJEbFFTMHg1TlU1dE9VbERSRFJEUzNsc2VrWTFUR2xTWTAxeVIyc3dVR3BwU1djME1FcEhjelJvZFRKUU0wOVdXbTlTU1UxTFdVSmthRGhxY0ZWbFRHZHNWR0V6ZURWd2JqVjZRV0U1UVRodE5sQmllWFphVW5OYWN6VTBkSFF3TTB0SFMyaFhjRFYwWmtWWWQxUnRhWGg0T1RkelkwVklXVkpLYUVoQ2NFVnNjVWs0TUZOalptVkpha3BZUW5WWmRUQk9NRGR2UjA5RVNXUkliME5EWDJsc2VrMXNXbUpIUXpsU1dWOVdTRm8wVUU5Q1FrbHJRMFE0VVhGb1JIZHRSMFZ5ZWtkNFdFdHVaWFk1ZG5GWE1VOVlRV3RsZVd4RGMwVktRMVJxYjAxRldsSTRabk5SUWtSeldWaG58CYWU_dsU1MWQugGVYq6Ja1_3Ky8vza7MRzR2AKUrLw8='
    value = 'eyJhbGciOiJSUzI1NiIsImtpZCI6IjU4ODI0YTI2ZjFlY2Q1NjEyN2U4OWY1YzkwYTg4MDYxMTJhYmU5OWMiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoiTW9zdGFwaGEgU2FkZWdoaXBvdXIgUm91ZHNhcmkiLCJwaWN0dXJlIjoiaHR0cHM6Ly9saDMuZ29vZ2xldXNlcmNvbnRlbnQuY29tL2EtL0FPaDE0R2dKMzc3ei1TUU82QmlseVFaMmpTaXdBWFJSQ3ZpZlhoQmhKS1FOYzFtRTUxVnB2N3dEaTFSTk1od2FfVENpTHhiUEdnZjhrRUh0V3kzWVZiUVpYUWsyVEdqUGZ1Y1Myc0JJZldIRFRtbTRtbUI3M2xYNHdhaU91XzBjTFJzRVRqTklwSEk2Vmd0Y2RWTlF1MUxjckpQRzItT1dlYmtWNEZjZ3oyMkdTcU50SkQzeVdSeUZiZXJMRXpabW5sbVBzVmFXeHdiM3V4aUFjeFBGU3J2LWdjcXEzeld3Z1c2MzVGV1VXWmhIOGVNbXVYWkF1ZFd0Y0FMUXZhbklRWHluNm50Ynp2VjFOMWZwZWtZZ0RKVHprNDQ5aGRDTm9OUHcyWGhOYURGbWx1N1FXOEJTYS1NLXk2M1k0X2R3UW9vVEFUMUhBRWRyQmhMNTEzNmhXUG1Rcl80RlBQcXJZeWRzb3MzdUc0M0NqXy11eWNlazgxVV8wLXloRGFRY1JEWUc2Q3ZaRWR5YWRyajdBakE2UjZwZ0h2MERjT056MUwxeEJrN2pkRndmZWkzNkp0S1NBT1RmYndzRl9rN0NnWU1Ba0MyYzJrM3FsVlpKdVJhdHhfT2Q3aFl3M2NCLURwNHpMX3J4TXNheTM3NGYtVjlyTVpBcXcwVGxNMkc5dmJFMXZ3TFhpcmFjZEdGTUtnRjZoT0dXclZYSTdyOG5zSFdUcDd3S2VXSXQxa0FMV25BOHVVRzdCTjd2d1lfdWdNeHdSNTZFcTBtM3hHWGh2eXpHRnpGTm8zWG5YekR1TXVnaC1nY0VBR0NHNjZJTjNVUGRyRE9TOXEtcjNOLWRRLThfWXlyYlNlZ0xuNHM5VURmbU81bW05WTlkQTQtRVZzVmdMRndqeE5VakZhekpYdGVfRUhOejJkcmZ0X3plZmZja3RXRmlpclZCcXpocW1jSXlJNFJ4ZnNETFdhWmtJSHlJOUpoeXJPYzR1NkhtOVZOLU9KUFdXZEM5cVR2VUNGOU9XUXV6WEE9czk2LWMiLCJhY2NvdW50IjoiZWEyMDFjYTctYzc4My00YjAzLWFiZTMtN2ExYTMzYWNmYTg0IiwiaXNzIjoiaHR0cHM6Ly9zZWN1cmV0b2tlbi5nb29nbGUuY29tL3BvbGxpbmF0aW9uLXN0YWdpbmctMWQ2YTgiLCJhdWQiOiJwb2xsaW5hdGlvbi1zdGFnaW5nLTFkNmE4IiwiYXV0aF90aW1lIjoxNjYyMTE2OTU4LCJ1c2VyX2lkIjoiT0oyTWlJa3M3T1VFQUZYRDFKaXl3V01OVHluMSIsInN1YiI6Ik9KMk1pSWtzN09VRUFGWEQxSml5d1dNTlR5bjEiLCJpYXQiOjE2NzgzOTc0MDcsImV4cCI6MTY3ODQwMTAwNywiZW1haWwiOiJtb3N0YXBoYUBsYWR5YnVnLnRvb2xzIiwiZW1haWxfdmVyaWZpZWQiOnRydWUsImZpcmViYXNlIjp7ImlkZW50aXRpZXMiOnsiZ29vZ2xlLmNvbSI6WyIxMTI5ODM1MDY3NjgwNjE1NzY2ODkiXSwiZW1haWwiOlsibW9zdGFwaGFAbGFkeWJ1Zy50b29scyJdfSwic2lnbl9pbl9wcm92aWRlciI6Imdvb2dsZS5jb20ifX0.d2c76dKQOaXNorM41LgAjp1F5XhDkXtzjap5fZx8exx1P0vI-MkSupz9d96G7fmzfohTwBEgBy9s1A91o85R_wzQ7ex4_YTslOGXzY3fyD9PKLy5Nm9ICD4CKylzF5LiRcMrGk0PjiIg40JGs4hu2P3OVZoRIMKYBdh8jpUeLglTa3x5pn5zAa9A8m6PbyvZRsZs54tt03KGKhWp5tfEXwTmixx97scEHYRJhHBpElqI80ScfeIjJXBuYu0N07oGODIdHoCC_ilzMlZbGC9RY_VHZ4POBBIkCD8QqhDwmGErzGxXKnev9vqW1OXAkeylCsEJCTjoMEZR8fsQBDsYXg'
    assert _decrypt_cookie(cookie) == value
