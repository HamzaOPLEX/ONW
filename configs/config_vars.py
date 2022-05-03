status = {
    'success': 1,
    'failed': 0,
}


custom_status_codes = {      
            'error':{
                    'ONW500':'record already exist',
                    'ONW501':"cannot delete this record because it's related to another objects",
                    'ONW502':'data not valid or not exist',
                    'ONW503':'missing required data fields',
                    'ONW504':'record not found',
                    },
            'success':{
                    'ONW200':'record added successfully',
                    'ONW201':'record updated successfully',
                    'ONW202':'record deleted successfully',
                    },
            'info':{
                    'ONW100':'please to fill all required fields',
                    },
        }