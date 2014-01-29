/*
 * struct.c
 * Minimal example to handle structs.
 *
 * This is a MEX-file for MATLAB.
 */

#include <mex.h>


/* the gateway routine */
void mexFunction(int nlhs, mxArray *plhs[], int nrhs, const mxArray *prhs[])
{
    /* check proper input and output */
    if (nrhs != 1)
        mexErrMsgIdAndTxt("struct:invalidNumInputs", "Only one input required.");
    else if (!mxIsStruct(prhs[0]))
        mexErrMsgIdAndTxt("struct:inputNotStruct", "Input must be a structure.");

    if (nlhs != 0)
        mexErrMsgIdAndTxt("struct:invalidNumOutputs", "No output required.");

    /* disclaimer: there should be other checks for the input */

    mwSize nfields = mxGetNumberOfFields(prhs[0]);
    mexPrintf("number of fields=%d\n", nfields);

    mxArray *parray = mxGetField(prhs[0], 0, "x");
    double *pdata = mxGetData(parray);
    mexPrintf("%.2f\n", *pdata);
}
