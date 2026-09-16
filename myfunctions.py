import pyperclip
import os
from pathlib import Path
import platform
import cleanpipe as cl
import subprocess

if platform.system() == "Windows":
    pass
else:
    pyperclip.set_clipboard("xclip") #please notice that in linux, xclip must be installed


def bunda(a, b, c):
    """This function concatenates a, b and c and sends the result to the clipboard."""

    
    concatenated = a + b + c


    # Copy text to the clipboard
    pyperclip.copy(concatenated)

    # Retrieve text from the clipboard
    sent = pyperclip.paste()


    return sent + " sent to clipboard"


def clipboard_hello_world():
    """This function sends 'echo 'Hello World !'' to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy("echo 'Hello World !'")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"




def clipboard_bashrc():
    """This function sends something to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(
r"""

conda activate bio

source /etc/profile.d/modules.sh
module purge
module load vmd
module load gromacs/2025


""")
    
    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"




def clipboard_os_info():
    """This function sends 'uname -a' to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy("uname -a")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_cpu_info():
    """This function sends 'lscpu' to the clipboard."""
    
    # Copy text to the clipboard
    #pyperclip.copy("lscpu")
    pyperclip.copy(r"""LC_ALL=C lscpu | awk -F: '/^Model name:/ {model=$2} /^CPU\(s\):/ {logical=$2} /^Thread\(s\) per core:/ {threads=$2} /^Core\(s\) per socket:/ {cores=$2} /^Socket\(s\):/ {sockets=$2} /^CPU max MHz:/ {mhz=$2} /^L3 cache:/ {l3=$2} /^NUMA node\(s\):/ {numa=$2} END {gsub(/^ +/,"",model); gsub(/^ +/,"",logical); gsub(/^ +/,"",threads); gsub(/^ +/,"",cores); gsub(/^ +/,"",sockets); gsub(/^ +/,"",mhz); gsub(/^ +/,"",l3); gsub(/^ +/,"",numa); printf "\nCPU model:      %s\n\n",model; printf "Max frequency:  %.2f GHz   # this is the max; in CPU model you can see the base frequency\n",mhz/1000; printf "Sockets:        %s\n",sockets; printf "Cores/Socket:   %s   # multiply this number by Sockets (above) to get physical cores\n",cores; printf "Threads/Core:   %s   # hyperthreading capability\n",threads; printf "Logical Cores:  %s   # maximum threads Linux can schedule (physical cores x Threads/Core)\n",logical; printf "L3 cache:       %s   # shared fast memory\n",l3; printf "NUMA nodes:     %s   # physical cores / NUMA nodes = cores sharing local RAM\n",numa}'""")



    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"

def clipboard_gpu_info():
    """This function sends a command to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy("nvidia-smi")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"

def clipboard_avalable_ram():
    """This function sends 'free -h' to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy("free -h")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_avalable_storage():
    """This function sends a text to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy("lsblk -f")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_filesystems_and_disk_space():
    """This function sends 'df -h' to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy("df -h")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_folders_and_disk_space(s_option):
    """This function sends 'du -hd1 .' to the clipboard."""
    
    if s_option == "folders sizes":
        pyperclip.copy("du -hd1 . | sort -hr")
    elif s_option == "5 largest files nested":
        pyperclip.copy(r"find . -type f -printf '%s\t%p\n' | sort -nr | head -n 5 | numfmt --field=1 --to=iec")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_ip():
    """This function sends 'echo -------Who am I on the network?------- && ip a && echo -------How do I reach other machines/networks?------- && ip route' to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(r"""echo "";PUB="$((curl -4 -fsS icanhazip.com || curl -4 -fsS ifconfig.co || curl -4 -fsS api.ipify.org) | grep -Eo '([0-9]{1,3}\.){3}[0-9]{1,3}' | head -n1)"; [ -z "$PUB" ] && PUB="(unknown)"; printf "Public IP        : %s\n" "$PUB"; ip -o -4 addr show up scope global | while read -r _ IF _ IPCIDR _; do IP="${IPCIDR%/*}"; PFX="${IPCIDR#*/}"; NM="$(awk -v p="$PFX" 'BEGIN{split("0 128 192 224 240 248 252 254 255",A," ");k1=p;k1=(k1>8?8:(k1<0?0:k1));k2=p-8;k2=(k2>8?8:(k2<0?0:k2));k3=p-16;k3=(k3>8?8:(k3<0?0:k3));k4=p-24;k4=(k4>8?8:(k4<0?0:k4));print A[k1]"."A[k2]"."A[k3]"."A[k4]}')"; GW="$(ip -4 route get 1.1.1.1 from "$IP" 2>/dev/null | awk '/via/ {for(i=1;i<=NF;i++) if($i=="via"){print $(i+1); exit}}')"; [ -z "$GW" ] && GW="$(ip -4 route show default dev "$IF" 2>/dev/null | awk '/^default/ {print $3; exit}')" ; [ -z "$GW" ] && GW="(none)"; printf "Local IP (%s): %s  mask %s (/%s)  gateway %s\n" "$IF" "$IP" "$NM" "$PFX" "$GW"; done""")
    
    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"



    
def clipboard_ports_listening():
    """This function sends something to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(r"""ss -tulpn""")
    
    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"

def clipboard_port_forwarding():
    """This function sends something to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(r"""ssh -L <local_port>:<remote_host>:<remote_port> <user>@<host>""")
    
    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"

def clipboard_start_server():
    """This function sends something to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(r"""python -m http.server <port>""")
    
    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"



def clipboard_ips_to_ssh():
    """This function sends 'echo -------Who am I on the network?------- && ip a && echo -------How do I reach other machines/networks?------- && ip route' to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(r"""echo "";while read -r ipcidr; do ip=${ipcidr%/*}; pfx=${ipcidr#*/}; IFS=. read -r a b c d <<<"$ip"; ipi=$(( (a<<24)+(b<<16)+(c<<8)+d )); mask=$(( pfx==0 ? 0 : (0xFFFFFFFF << (32-pfx)) & 0xFFFFFFFF )); net=$(( ipi & mask )); bcast=$(( net | (~mask & 0xFFFFFFFF) )); for ((n=net+1; n<bcast; n++)); do A=$(( (n>>24)&255 )); B=$(( (n>>16)&255 )); C=$(( (n>>8)&255 )); D=$(( n&255 )); tgt="$A.$B.$C.$D"; (echo >/dev/tcp/$tgt/22) >/dev/null 2>&1 && { hn=$(getent hosts "$tgt" | awk '{print $2}' | head -n1); printf "%-15s\t%s\n" "$tgt" "${hn:--}"; }; done; done < <(ip -o -4 addr show scope global | awk '{print $4}')""")
    
    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"




def clipboard_ssh_send_key_to_server():
    """This function sends something to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(r"""ssh-copy-id -i ~/.ssh/id_ed25519.pub <user>@<host>""")
    
    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"



def clipboard_ssh_alias():
    """This function sends something to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(
r"""

Host chestnut                         
    HostName ibcp24-083.ibcp.fr
    User hrigitano

Host oxygen
    HostName oxygen
    User hrigitano

## bridge to external supercomputers

Host ibcp3245
    HostName ibcp3245

ControlMaster auto
ControlPath   /home/hrigitano/.ssh/tmp/%h_%p_%r

## external supercomputers

Host rome
    HostName irene-amd-fr.ccc.cea.fr
    User decarvah
    ProxyCommand ssh -W %h:%p ibcp3245

Host adastra
    HostName adastra.cines.fr
    User hrigitano
    ProxyCommand ssh -W %h:%p ibcp3245

""")
    
    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"



def clipboard_file_transfer(s_choice,s_extension):
    """This function sends something to the clipboard."""
    
    if s_choice == 'folder':
        pyperclip.copy(f"""rsync -avz hrigitano@ibcp24-043:/data1/sonia/folder_without_slash .""")

    elif s_choice == 'chosen extension, keeping folder structure':
        pyperclip.copy(f"""rsync -avm --include='*/' --include='*.{s_extension}' --exclude='*' hrigitano@ibcp24-043:/data1/sonia/folder_without_slash .""")
    
    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"





def clipboard_custer_overview():
    """This function sends something to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(r'sinfo -N -o "%20N %15P %8c %12m %20G %10T"')
    
    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"



def clipboard_make_executable(s_etapa):
    """
    The value of s_etapa was chosen in a dropdown menu in the frontend
    This function sends to the clipboard. one of the following commands, depending on the value of s_etapa: 
       '#!/bin/bash'
       '#!/bin/env python' this make sure the script will run with the python interpreter FROM THE ACTIVE ENVIRONMENT
       'chmod +x nomeDoArquivo' 
       'export PATH='/bla/bla/nomeDaPasta:$PATH'
    """
    
    # Copy text to the clipboard, depending on the value of s_etapa
    if s_etapa == "shebang - interpreter will be bash":
        pyperclip.copy("#!/bin/bash")

    elif s_etapa == "shebang - interpreter will be python":
        pyperclip.copy("#!/bin/env python")

    elif s_etapa == "chmod - make executable":
        pyperclip.copy("chmod +x nomeDoArquivo")

    elif s_etapa == "export - add folder to PATH to call it directly":

        pyperclip.copy("export PATH='/caminho/caminho/nomeDaPasta:$PATH'")

    else:
        raise ValueError("Invalid value for s_etapa")


    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_see_content_of_path_variable():
    """This function sends 'echo "$PATH" | tr ':' '\n'' to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy("echo \"$PATH\" | tr ':' '\\n'")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"



# xxx execute, monitor execution, kill execution




def clipboard_python_location():
    """This function sends 'which python' to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy("which python")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_modules_location():
    """This function sends to the clipboard a huge coomand to see modules are instaled to and imported from ."""
    
    # Copy text to the clipboard
    pyperclip.copy("python -c \"import sys,sysconfig; print('\\nINSTALL\\n\\n',sysconfig.get_paths()['purelib']); print('\\nIMPORT'); print('\\n'.join(sys.path))\"")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"



def clipboard_see_all_conda_environments():
    """This function sends 'conda env list' to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy("conda env list")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"



def clipboard_create_conda_environment(s_env_name,s_python_version):
    """This function sends 'conda create --name nomeDoAmbiente python=3.9' to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"conda create --name {s_env_name} python={s_python_version}")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"






def clipboard_minimal_scheduler_file(s_choice):
    """This function sends a string to the clipboard."""
    
    # Copy text to the clipboard
    if s_choice == "slurm":

        pyperclip.copy(f"""
#!/bin/bash

#SBATCH --partition=calcul 
#SBATCH --nodes=1

                              #       gmx          #    gmx_mpi (alows for multiple nodes)
#SBATCH --ntasks=1            #        1           #    must mach: mpirun -np foo gmx_mpi
#SBATCH --cpus-per-task=24    #   -ntomp x -ntmp   #              -ntomp
#SBATCH --gres=gpu:1          #        1           #          must match ntasks

#SBATCH --job-name=continue
#SBATCH --output=outanderr.continue.slurm.txt

##SBATCH --nodelist=node-20
##SBATCH --exclude=node-15


module purge
module load gromacs/2025.4

# ---- 24h-wall self-chaining : queue the follow-up job now ----
# If production is already finished, stop the chain (done.txt is made in post-processing).
if [[ -f "done.txt" ]]; then
    echo "Simulation already complete. Exiting."
    exit 0
fi
# Otherwise queue the NEXT copy of this job, to start when THIS one ends OK.
THIS_SCRIPT_PATH="$(readlink -f "$0")"
sbatch --dependency=afterany:$SLURM_JOB_ID "$THIS_SCRIPT_PATH"
# --------------------------------------------------------------




#insert the command here



#insert some sort of theck to see if the command concluded, sanding a "done.txt" file




""")

    elif s_choice == "rome":

        pyperclip.copy(f"""
#!/bin/bash

#MSUB   -r mdrun       # Job name
#MSUB   -n 1                       # Number of tasks in parallel mode (-ntmpi)
#MSUB   -c 1                       # Number of cores per parallel task (-ntomp) this should also be exported
#MSUB   -W yes                     # Let multiple jobs sharing same name & user run simultaneously
#MSUB   -o out.continue.scheduler.%I.txt            # Output file
#MSUB   -e err.continue.scheduler.%I.txt            # Output file for errors
#MSUB   -q rome                    # Partition:    rome        
#MSUB   -A gen13458                # Project code: gen10138 or spe00017
#MSUB   -m scratch,work,store      # File system:  scratch,work,store
#MSUB   -Q normal                  # Quality of Service (test,normal,long) (ccc_mqinfo)
#MSUB   -T 86400                   # Maximum walltime in seconds

set -x                      # echo commands

module purge                # retire tous les modules déchargeables de l'environnement
module load gnu/11          # charge gnu/11 et définit gnu/11 comme compilateur dans votre environnement
module load nvhpc/24.3      # besoin de mettre avant OpenMPI comme ce dernier charge un cuda qui n'est pas compatible avec nvhpc/24.3
module load mpi/openmpi/4   # charge la souche OpenMPI
module load gromacs/2025.0  # charge le produit

export GMX_DISABLE_GPU_DETECTION=1  # prevent GROMACS from using GPUs
export I_MPI_PIN_CELL=core
export I_MPI_PIN_DOMAIN=auto

export OMP_NUM_THREADS=32                  # number of OpenMP threads (-ntomp)
export OMP_DYNAMIC=FALSE




""")



    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"



def clipboard_hpc_send(s_choice):
    """This function sends a string to the clipboard."""
    
    # Copy text to the clipboard
    if s_choice == "rome":
        pyperclip.copy(f"rsync -avz --chmod=Dg+s --chown=:gen13458 folder_without_slash rome:/ccc/work/cont003/gen13458/decarvah/")
    elif s_choice == "adastra":
        pyperclip.copy(f"rsync -avz folder_without_slash adastra:/scratch/CT7/c1613458/hrigitano/")



    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_hpc_bring(s_choice):
    """This function sends a string to the clipboard."""
    
    # Copy text to the clipboard
    if s_choice == "rome":
        pyperclip.copy(f"rsync -avz rome:/ccc/work/cont003/gen13458/decarvah/folder_without_slash .")
    elif s_choice == "adastra":
        pyperclip.copy(f"rsync -avz adastra:/scratch/CT7/c1613458/hrigitano/folder_whithout_slash .")




    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"

def clipboard_hpc_see(s_choice):
    """This function sends a string to the clipboard."""
    
    # Copy text to the clipboard
    if s_choice == "rome":
        pyperclip.copy(f"ccc_mpp -u decarvah")
    elif s_choice == "slurm":
        pyperclip.copy(f"squeue -u $USER -o \"%.18i %.9P %.8j %.8u %.2t %.10M %.6D %R %C %b\"")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"

def clipboard_hpc_kill():
    """This function sends a string to the clipboard."""
    

    pyperclip.copy(f"scancel -u $USER")


    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_assess_busyness():
    """This function sends a string to the clipboard."""
    

    pyperclip.copy(r"""ccc_mpp -p -q rome -n | awk 'NR>1 {jobs++; cores+=$4} END {printf "Pending jobs: %d\nPending requested cores: %d\n", jobs, cores}'""")


    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"



def clipboard_hpc_hours(s_choice):
    """This function sends a string to the clipboard."""
    

    # Copy text to the clipboard
    if s_choice == "rome":
        pyperclip.copy(f"ccc_myproject")
    elif s_choice == "adastra":
        pyperclip.copy(f"xxxxxx")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"

def clipboard_keygen(s_chosen_action,s_chosen_protocol):
    """This function sends a comand to the clipboard, depending on s_chosen_action and s_chosen_protocol.
    
    # Ed25519 (modern, shorter keys, more secure)
    cat ~/.ssh/id_ed25519.pub
    ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519

    # OR, RSA 4096-bit (older systems / some services still require RSA)
    cat ~/.ssh/id_rsa.pub
    ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_rsa
    
    
    """
    
    # Copy text to the clipboard, depending on the value of s_chosen_action and s_chosen_protocol
    if s_chosen_action == "see":

        if s_chosen_protocol == "Ed25519 (modern)":
            pyperclip.copy(f"cat ~/.ssh/id_ed25519.pub")

        elif s_chosen_protocol == "RSA (older systems)":
            pyperclip.copy(f"cat ~/.ssh/id_rsa.pub")
        else:
            raise ValueError("Invalid value for s_chosen_protocol")

    elif s_chosen_action == "generate":

        if s_chosen_protocol == "Ed25519 (modern)":
            pyperclip.copy(f"ssh-keygen -t ed25519 -f ~/.ssh/id_ed25519")

        elif s_chosen_protocol == "RSA (older systems)":
            pyperclip.copy(f"ssh-keygen -t rsa -b 4096 -f ~/.ssh/id_rsa")

        else:
            raise ValueError("Invalid value for s_chosen_protocol")

    else:
        raise ValueError("Invalid value for s_chosen_action")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"



def clipboard_init_or_clone(s_chosen_action,s_repo_link):
    """This function sends a big commant to the clipboard. depending on the value of s_chosen_action."""
    



    # Copy text to the clipboard, depending on the value of s_chosen_action and s_chosen_action
    if s_chosen_action == "init (project started localy)":
        pyperclip.copy("git init --initial-branch=main && git add . && git commit -m 'Initial commit' && git remote add origin https://github.com/rigitano/$(basename \"$PWD\").git && git push -u origin main")

    elif s_chosen_action == "clone (project started at github)":
        pyperclip.copy(f"git clone {s_repo_link}")

    else:
        raise ValueError("Invalid value for s_chosen_action")




    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"



def clipboard_pull():
    """This function sends 'git pull origin main' to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy("git pull origin main")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_add_commit(s_message):
    """This function sends git add . && git commit -m 'xxx' to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"git add . && git commit -m '{s_message}'")


    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_add_commit_new_branch(s_new_branch_name,s_message):
    """This function sends git checkout -b 'xxx' && git add . && git commit -m 'xxx' to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"git checkout -b '{s_new_branch_name}' && git add . && git commit -m '{s_message}'")


    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"



def clipboard_push():
    """This function sends 'git push origin main' to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy("git push origin main")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"

def clipboard_checkout(s_commit_hash):
    """This function sends a text to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"git checkout '{s_commit_hash}'")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_go_back(s_commit_hash,s_option):
    """This function goes back to a commit, it will erase the ones after it or not depending on the value of s_option."""
    
    # Copy text to the clipboard, depending on the value of s_option
    if s_option == "reset --hard (DANGER: all posterior changes and commits will be deleted!)":
        pyperclip.copy(f"git reset --hard '{s_commit_hash}'")

    elif s_option == "revert (posterior commits will be kept, a new commit will be created with the same code as the chosen commit)":
        pyperclip.copy(f"git revert '{s_commit_hash}'..HEAD")

    else:
        raise ValueError("Invalid value for s_option")


    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_stash(s_message):
    """This function sends git stash push -m 'xxxxxx' to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"git stash push -m '{s_message}'")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_see_all_branches():
    """This function sends 'git branch' to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy("git branch")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_change_branch(s_branch_name):
    """This function sends text to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"git checkout {s_branch_name}")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_merge(s_source_branch_with_extra_code,s_destination_branch):
    """This function sends 'git checkout xxx && git merge xxx --no-ff' to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"git checkout {s_destination_branch} && git merge {s_source_branch_with_extra_code} --no-ff")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"







def clipboard_search_filesystem(s_by_what, s_search_for_this):
    """This function sends codes to the clipboard, depending on the choice made on a droplist."""
    
    # Copy text to the clipboard, depending on the value of s_by_what
    if s_by_what == "in the file name":
        pyperclip.copy(rf"find . -type f -printf '%p\t%f\n' | awk -v pat='{s_search_for_this}' -F '\t' '$2 ~ pat {{print $1}}'")

    elif s_by_what == "entire path+name":
        pyperclip.copy(f"find . -type f -regextype posix-extended -regex \".*{s_search_for_this}.*\"")

    elif s_by_what == "in the file content":
        pyperclip.copy(f"find . -type f -print | xargs egrep \"{s_search_for_this}\"")

    else:
        raise ValueError("Invalid value for s_by_what")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_extraction(s_file_name,s_choice,):
    """This function sends a command to the clipboard depending on s_file_name."""
    
    # Copy text to the clipboard, depending on the value of s_choice
    if s_choice == ".tar":
        pyperclip.copy(f"tar -xvf {s_file_name}")

    elif s_choice == ".tar.gz":
        pyperclip.copy(f"tar -xzvf {s_file_name}")

    elif s_choice == ".tar.bz2":
        pyperclip.copy(f"tar -xjvf {s_file_name}")

    elif s_choice == ".tar.xz":
        pyperclip.copy(f"tar -xJvf {s_file_name}")

    elif s_choice == ".gz":
        pyperclip.copy(f"gunzip -k {s_file_name}")

    elif s_choice == ".bz2":
        pyperclip.copy(f"bunzip2 -k {s_file_name}")

    elif s_choice == ".xz":
        pyperclip.copy(f"unxz -k {s_file_name}")


    else:
        raise ValueError("Invalid value for s_choice")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_compression(s_in_file_name, s_choice):
    """This function sends a command to the clipboard depending on s_file_name."""
    
    # Copy text to the clipboard, depending on the value of s_choice
    if s_choice == ".tar":
        pyperclip.copy(
            f'dir="{s_in_file_name}"; '
            'dir="${dir/#\\~/$HOME}"; '
            'dir_resolved=$(cd "$dir" 2>/dev/null && pwd -P) || exit 1; '
            'name=$(basename "$dir_resolved"); '
            'pwd_resolved=$(pwd -P); '
            'exclude=(); '
            '[[ "$dir_resolved" == "$pwd_resolved" ]] && exclude=(--exclude="$name.tar"); '
            'tar -cf "$name.tar" "$dir" "${exclude[@]}"'
        )

    elif s_choice == ".tar.gz":
        pyperclip.copy(
            f'dir="{s_in_file_name}"; '
            'dir="${dir/#\\~/$HOME}"; '
            'dir_resolved=$(cd "$dir" 2>/dev/null && pwd -P) || exit 1; '
            'name=$(basename "$dir_resolved"); '
            'pwd_resolved=$(pwd -P); '
            'exclude=(); '
            '[[ "$dir_resolved" == "$pwd_resolved" ]] && exclude=(--exclude="$name.tar.gz"); '
            'tar -czf "$name.tar.gz" "$dir" "${exclude[@]}"'
        )

    elif s_choice == ".tar.bz2":
        pyperclip.copy(
            f'dir="{s_in_file_name}"; '
            'dir="${dir/#\\~/$HOME}"; '
            'dir_resolved=$(cd "$dir" 2>/dev/null && pwd -P) || exit 1; '
            'name=$(basename "$dir_resolved"); '
            'pwd_resolved=$(pwd -P); '
            'exclude=(); '
            '[[ "$dir_resolved" == "$pwd_resolved" ]] && exclude=(--exclude="$name.tar.bz2"); '
            'tar -cjf "$name.tar.bz2" "$dir" "${exclude[@]}"'
        )

    elif s_choice == ".tar.xz":
        pyperclip.copy(
            f'dir="{s_in_file_name}"; '
            'dir="${dir/#\\~/$HOME}"; '
            'dir_resolved=$(cd "$dir" 2>/dev/null && pwd -P) || exit 1; '
            'name=$(basename "$dir_resolved"); '
            'pwd_resolved=$(pwd -P); '
            'exclude=(); '
            '[[ "$dir_resolved" == "$pwd_resolved" ]] && exclude=(--exclude="$name.tar.xz"); '
            'tar -cJf "$name.tar.xz" "$dir" "${exclude[@]}"'
        )

    elif s_choice == ".gz":
        pyperclip.copy(f"gzip -k {s_in_file_name}")

    elif s_choice == ".bz2":
        pyperclip.copy(f"bzip2 -k {s_in_file_name}")

    elif s_choice == ".xz":
        pyperclip.copy(f"xz -k {s_in_file_name}")


    else:
        raise ValueError("Invalid value for s_choice")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()



def clipboard_execute(s_choice):
    """This function sends a coomand to the clipboard depending on the choice on the dropbox."""

    # Copy text to the clipboard, depending on the value of s_choice
    if s_choice == "bash (./)":
        pyperclip.copy(f"./")

    elif s_choice == "nextflow (nextflow run)":
        pyperclip.copy(f"nextflow run ")

    elif s_choice == "docker (docker run -d)":
        pyperclip.copy(f"docker run -d ")

    elif s_choice == "slurm (sbatch)":
        pyperclip.copy(f"sbatch ")

    elif s_choice == "torque (qsub)":
        pyperclip.copy(f"qsub ")

    elif s_choice == "moab on top of torque (msub)":
        pyperclip.copy(f"msub ")

    elif s_choice == "kubernetes (kubectl apply -f)":
        pyperclip.copy(f"kubectl apply -f ") 

    elif s_choice == "yarn-hadoop (yarn jar)":
        pyperclip.copy(f"yarn jar ") 

    elif s_choice == "spark on top of yarn-hadoop (spark-submit --master yarn)":
        pyperclip.copy(f"spark-submit --master yarn ") 


    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_see_running_processes(s_choice):
    """This function sends a coomand to the clipboard depending on the choice on the dropbox."""
    


    # Copy text to the clipboard, depending on the value of s_choice
    if s_choice == "bash (top)":
        pyperclip.copy(f"top")

    elif s_choice == "nextflow (nextflow log)":
        pyperclip.copy(f"nextflow log")

    elif s_choice == "docker (docker ps)":
        pyperclip.copy(f"docker ps")

    elif s_choice == "slurm (squeue)":
        pyperclip.copy(f"squeue")

    elif s_choice == "torque (qstat)":
        pyperclip.copy(f"qstat")

    elif s_choice == "moab on top of torque (showq)":
        pyperclip.copy(f"showq")

    elif s_choice == "kubernetes (kubectl get pods)":
        pyperclip.copy(f"kubectl get pods") 

    elif s_choice == "yarn-hadoop (yarn application -list)":
        pyperclip.copy(f"yarn application -list") 

    elif s_choice == "spark on top of yarn-hadoop (use UI!)":
        pyperclip.copy(f"use UI!") 


    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_cancel_execution(s_choice):
    """This function sends a coomand to the clipboard depending on the choice on the dropbox."""
    


    # Copy text to the clipboard, depending on the value of s_choice
    if s_choice == "bash (kill)":
        pyperclip.copy(f"kill ")

    elif s_choice == "nextflow (nextflow kill)":
        pyperclip.copy(f"nextflow kill ")

    elif s_choice == "docker (docker stop)":
        pyperclip.copy(f"docker stop ")

    elif s_choice == "slurm (scancel)":
        pyperclip.copy(f"scancel ")

    elif s_choice == "torque (qdel)":
        pyperclip.copy(f"qdel ")

    elif s_choice == "moab on top of torque (mjobctl -c)":
        pyperclip.copy(f"mjobctl -c ")

    elif s_choice == "kubernetes (kubectl delet pod)":
        pyperclip.copy(f"kubectl delet pod ") 

    elif s_choice == "yarn-hadoop (yarn application -kill)":
        pyperclip.copy(f"yarn application -kill ") 

    elif s_choice == "spark on top of yarn-hadoop (yarn application -kill)":
        pyperclip.copy(f"yarn application -kill ") 


    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"



def clipboard_find(s_word_to_find,s_file_to_be_searched):
    """This function sends 'grep -n 'henrique' file.txt' to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"grep -n '{s_word_to_find}' {s_file_to_be_searched}")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_replace(s_old_value,s_new_value,s_file_with_text,s_new_file_name):
    """This function sends text to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"sed 's/{s_old_value}/{s_new_value}/g' {s_file_with_text} > {s_new_file_name}")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"



def clipboard_find_vim(s_word_to_find):
    """This function sends a text to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"/{s_word_to_find}")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_replace_vim(s_old_value,s_new_value):
    """This function sends a text  to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"%s/{s_old_value}/{s_new_value}/gc")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"




def clipboard_fiter_table_bash(s_value_to_be_filtered, s_file_name,s_column):
    """This function sends a command to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"awk '${s_column} == \"{s_value_to_be_filtered}\"' {s_file_name}")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"

def clipboard_sort_table_bash(s_file_name,s_column,s_type):
    """This function sends a command to the clipboard."""
    
    # Copy text to the clipboard
    if s_type == 'lexical':
        pyperclip.copy(f"sort -k{s_column},{s_column} {s_file_name}")
    elif s_type == 'numerical':
        pyperclip.copy(f"sort -k{s_column},{s_column}n {s_file_name}")
    else:
        print('choice doesnt exist')

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"



def clipboard_unique_lines_bash(s_file_name):
    """This function sends 'sort data.txt | uniq' to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"sort {s_file_name} | uniq")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"



def clipboard_parse_bash(s_regex,s_column_setup, s_file):
    """This function sends 'sort data.txt | uniq' to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"sed -E 's|{s_regex}|{s_column_setup}|' {s_file}")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"




def clipboard_minimaltop(s_ff, s_mol_itp, s_molname):
    """
    Creates a minimal GROMACS topology file and sends it to the clipboard.
    """

    pyperclip.copy(f"""

#include "{s_ff}"
#include "{s_mol_itp}"

[ system ]
nice system

[ molecules ]
; name          qt
{s_molname}     1
""")

    sent = pyperclip.paste()
    return sent + " sent to clipboard"







def clipboard_molecule2molecule_in_solvent(molecule, s_outSytemName, s_solvent, s_forceField, s_boxSize, s_maxsol, s_extra):
    """This function sends a python function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"cl.molecule2molecule_in_solvent({molecule}, {s_outSytemName}, {s_solvent}, {s_forceField}, {s_boxSize}, {s_maxsol}, {s_extra})")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"

def clipboard_molecule2molecule_in_water_and_oil(molecule, s_oil_option, s_outSytemName, s_forceField, s_boxSize,s_maxsolW, s_maxsolO, s_aditional_arguments):
    """This function sends a python function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"cl.molecule2molecule_in_water_and_oil({molecule},{s_oil_option} {s_outSytemName}, {s_forceField}, {s_boxSize}, {s_maxsolW}, {s_maxsolO}, s_aditional_arguments={s_aditional_arguments})")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"

def clipboard_molecule2box_full_of_that(s_pdbfile, s_forceField, s_box_size, n_mol):
    """This function sends a python function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"cl.molecule2box_full_of_that({s_pdbfile}, {s_forceField}, {s_box_size}, {n_mol})")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"



def clipboard_build_membrane(s_system_name):
    """Copy a build_membrane example to the clipboard."""

    text = f"""
lipid_domains = {{
# domain_id   lipid   ratio_out  ratio_in  APL
         0: [("POPC", 0.5,       0.5,      0.64),
             ("POPE", 0.5,       0.5,      0.52)],
         1: [("CHOL", 1,         1,        0.45)]
}}

floating_domains = [
    {{"domain_id": 1, "radius": 8, "points": [200, 450]}}
]

shape_params = {{
    "Box": (50, 50, 50),
    "Thickness": 4,
    "WallDensity": (1, 1),
    "Radius": 20,
}}

cl.build_membrane(
    out_system_name="{s_system_name}",
    shape_type="Sphere",
    shape_params=shape_params,
    lipids_by_domain=lipid_domains,
    floating_domains=floating_domains,
)
"""

    pyperclip.copy(text)

    return "Membrane build code sent to clipboard"

def clipboard_build_slab(s_system_name):
    """Copy a build_membrane example to the clipboard."""

    text = f"""
cl.slab_in_water(
    gro_in="box_full_of_ETOH.gro",
    top_in="box_full_of_ETOH.top",
    s_forceField="charmm36-jul2022",
    layer_thickness=3.0,              
    out_dir="{s_system_name}",
)
"""

    pyperclip.copy(text)

    return "Slab build code sent to clipboard"

def clipboard_pdb2gmx():
    """This function sends a python function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"gmx pdb2gmx -f .pdb -o .gro -p .top -missing -ter -ignh -water none -ff ../charmm36-jul2022")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"

def clipboard_editconf():
    """This function sends a python function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f'gmx editconf -f .gro -o .gro -c -box "3 3 3" -bt cubic')

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"

def clipboard_solvate(s_option):
    """This function sends a python function with arguments to the clipboard."""
    
    if s_option == "water":
        # Copy text to the clipboard
        pyperclip.copy(f"gmx solvate -cp something_in_vacum.gro -cs spc216.gro -maxsol 123 -o output.gro -p throughtput.top")
    elif s_option == "custom box":
        pyperclip.copy(f"gmx solvate -cp something_in_vacum.gro -cs custom_box.gro -o output.gro -p throughtput.top")


    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"

def clipboard_grompp():
    """This function sends a python function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"gmx grompp -f .mdp -c .gro -r .gro -p .top -o .tpr -maxwarn 1")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_mdrun(s_option):
    """This function sends a python function with arguments to the clipboard."""
    
    if s_option == "normal":
        pyperclip.copy(f"gmx mdrun -v -deffnm xxxx")
    elif s_option == "continue":
        pyperclip.copy(f"gmx mdrun -v -deffnm prod -cpi -nt 16")
    elif s_option == "extend":
        pyperclip.copy(f"gmx convert-tpr -s prod.tpr -extend 100000 -o extended.tpr && gmx mdrun -v -s extended.tpr -deffnm prod -cpi ")


    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_trjconv(s_option):
    """This function sends a python function with arguments to the clipboard."""

    if s_option == "generate last_step.gro":
        pyperclip.copy(f"gmx trjconv -s prod.tpr -f prod.xtc -o last_step.gro -dump 999999999")

    elif s_option == "center":
        pyperclip.copy(f"gmx trjconv -s prod.tpr -f prod.xtc -o prod.centered.xtc -center -pbc mol")

    elif s_option == "fit":
        pyperclip.copy(f"gmx trjconv -s prod.tpr -f prod.centered.xtc -o prod.fitted.xtc -fit progressive")


    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"




def clipboard_fit():
    """This function sends a python function with arguments to the clipboard."""
    
    # Copy text to the clipboard

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"

def clipboard_energy(s_option):
    """This function sends a python function with arguments to the clipboard."""
    
    if s_option == "(menu)":
        pyperclip.copy(r"gmx energy -f prod.edr -b 20000 -o edr_output20toEND.xvg")
    elif s_option == "Density":
        pyperclip.copy(r"""printf 'Density\n\n' | gmx energy -f prod.edr -b 20000 -o energy_density20toEND.xvg &> outanderr.energy.density20toEND""")
    elif s_option == "Temperature":
        pyperclip.copy(r"""printf 'Temperature\n\n' | gmx energy -f prod.edr -b 20000 -o energy_temperature20toEND.xvg &> outanderr.energy.temperature20toEND""")
    elif s_option == "Pressure":
        pyperclip.copy(r"""printf 'Pressure\n\n' | gmx energy -f prod.edr -b 0 -20000 energy_pressure20toEND.xvg &> outanderr.energy.pressure20toEND""")
    elif s_option == "Potential":
        pyperclip.copy(r"""printf 'Potential\n\n' | gmx energy -f prod.edr -b 0 -20000 energy_potential20toEND.xvg &> outanderr.energy.potential20toEND""")
    elif s_option == "#Surf*SurfTen":
        pyperclip.copy(r"""printf '#Surf*SurfTen\n\n' | gmx energy -f prod.edr -b 20000 -o energy_st20toEND.xvg &> outanderr.energy.st20toEND""")


    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"






def clipboard_runREALISTIC(s_suffix, s_gro, s_top, s_time, n_temperature, s_ff, s_machine, s_ntOMP, ntMPI ):
    """This function sends codes to the clipboard, depending on the choice made on a droplist."""
    

    pyperclip.copy(f"./runREALISTIC.sh {s_suffix} {s_gro} {s_top} {s_time} {n_temperature} {s_ff} {s_machine} {s_ntOMP} {ntMPI}")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_runBENCHMARK(s_machine, s_tpr):
    """This function sends codes to the clipboard, depending on the choice made on a droplist."""
    
    # Copy text to the clipboard, depending on the value of s_by_what
    if s_machine == "local":
        pyperclip.copy(f"./runBENCHMARK-local {s_tpr}")

    elif s_machine == "oxygen":
        pyperclip.copy(f"xxxxx")

    elif s_machine == "rome (moab wrapper with time limit)":
        pyperclip.copy(f"./runBENCHMARK-rome {s_tpr}")

    else:
        raise ValueError("Invalid value for s_machine")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_runFEPoff(s_suffix, s_gro, s_top, s_time, n_temperatures, s_ff, s_machine, s_molecule_to_decouple, s_ntOMP, ntMPI ):
    """This function sends codes to the clipboard, depending on the choice made on a droplist."""
    
    pyperclip.copy(f"./runFEPoff.sh {s_suffix} {s_gro} {s_top} {s_time} {n_temperatures} {s_ff} {s_machine} {s_molecule_to_decouple} {s_ntOMP} {ntMPI}")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"

def clipboard_runREPLEX(s_suffix, s_gro, s_top, s_time, s_tmin, s_tmax, s_ff, s_machine, s_ntOMP, ntMPI ):
    """This function sends codes to the clipboard, depending on the choice made on a droplist."""
    
    pyperclip.copy(f"./runREPLEX.sh {s_suffix} {s_gro} {s_top} {s_time} {s_tmin} {s_tmax} {s_ff} {s_machine} {s_ntOMP} {ntMPI}")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"




def clipboard_livestream():
    """This function sends a text to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"ssh rome 'tail -c +0 -f vis.xtc' | vmd -e visualize.vmd")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_download_and_clean_pdb(s_molecule_name):
    """This function sends a python function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"cl.download_and_clean_pdb({s_molecule_name})")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"

def clipboard_create_peptide(s_aminoacids, l_phi, l_psi_im1, s_nTerminusCAP, s_cTerminusCAP, s_outName ):
    """This function sends a python function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"cl.create_peptide({s_outName}, {s_aminoacids}, {l_phi}, {l_psi_im1}, {s_nTerminusCAP}, {s_cTerminusCAP} )")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"



def clipboard_insert_new_molecule_into_pdb(input_pdb, new_molecule_atoms, output_pdb):
    """This function sends a python function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"cl.insert_new_molecule_into_pdb({input_pdb}, {output_pdb}, {new_molecule_atoms})")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_insert_residue_into_chain(s_input_pdb_file,s_chain,n_residue,s_new_residue_name, d_new_residue_atoms,s_replace_or_displace,s_output_pdb_file):
    """This function sends a python function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"cl.insert_residue_into_chain({s_input_pdb_file},{s_output_pdb_file},{s_chain},{n_residue},{s_new_residue_name}, {d_new_residue_atoms},{s_replace_or_displace})")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_insert_atom_into_residue(s_input_pdb_file,s_chain,n_residue,s_atom_structural_name,s_atom_element_name,l_coord,s_output_pdb_file):
    """This function sends a python function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"cl.insert_atom_into_residue({s_input_pdb_file}, {s_output_pdb_file}, {s_chain}, {n_residue}, {s_atom_structural_name}, {s_atom_element_name}, {l_coord})")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_add_truss(s_pdb_file, p1, p2, n_square_size, s_out_pdb_file):
    """This function sends a python function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"cl.add_truss({s_pdb_file}, {s_out_pdb_file}, {p1}, {p2}, {n_square_size})")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"





def clipboard_freeze_dihedrals(s_potential_option, s_gro_file,s_top_file, restraining_force, s_molename, s_file_to_be_edited, s_out_file_name, s_which_dihedrals_option):
    """This function sends a cleanpipe function with arguments to the clipboard
    
    
    """
    
    # Copy text to the clipboard, depending on the value of s_potential_option and s_which_dihedrals_option
    if s_potential_option == "[ dihedrals ] type 2 (improper dihedral harmonic)" and s_which_dihedrals_option == "all":
        pyperclip.copy(f"xxxx")

    elif s_potential_option == "[ dihedrals ] type 2 (improper dihedral harmonic)" and s_which_dihedrals_option == "just phi and psi of protein":
        pyperclip.copy(f"cl.freeze_phi_psi_dihedrals({s_gro_file}, {s_top_file}, {restraining_force}, {s_molename}, {s_file_to_be_edited}, {s_out_file_name})")

    elif s_potential_option == "[ dihedrals ] type 4 (improper dihedral periodic)" and s_which_dihedrals_option == "all":
        pyperclip.copy(f"xxxx")

    elif s_potential_option == "[ dihedrals ] type 4 (improper dihedral periodic)" and s_which_dihedrals_option == "just phi and psi of protein":
        pyperclip.copy(f"xxxx")

    elif s_potential_option == "[ dihedral_restraints ] type 1 (a potential similar to improper dihedral)" and s_which_dihedrals_option == "all":
        pyperclip.copy(f"xxxx")

    elif s_potential_option == "[ dihedral_restraints ] type 1 (a potential similar to improper dihedral)" and s_which_dihedrals_option == "just phi and psi of protein":
        pyperclip.copy(f"xxxx")

    else:
        raise ValueError("Invalid values of s_potential_option or s_which_dihedrals_option")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_get_atom_global_id(s_top_file, s_molecule_name, n_molecule_instantiation, n_residue, s_atom):
    """This function sends a cleanpipe function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"id_atom = cl.get_atom_global_id({s_top_file}, {s_molecule_name}, {n_molecule_instantiation}, {n_residue}, {s_atom})")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"




def clipboard_basic_infos_of_molecules(s_top):
    """This function sends a cleanpipe function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"dd_mols_basic_infos = cl.basic_infos_of_molecules({s_top})")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"



def clipboard_getMoleculeName(s_top, n_order):
    """This function sends a cleanpipe function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"s_mol_name = cl.getMoleculeName({s_top}, order={n_order})")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_getSystemName(s_top):
    """This function sends a cleanpipe function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"s_system_name = cl.getSystemName({s_top})")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"




def clipboard_parse_directive(s_top, s_directive_name):
    """This function sends a cleanpipe function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"ll_parsed_directive = cl.parse_directive({s_top}, {s_directive_name})")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_parse_directives_inside_each_and_every_molecule(s_top):
    """This function sends a cleanpipe function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"dd_mols = cl.parse_directives_inside_each_and_every_molecule({s_top})")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_parse_directives_inside_intermolecular_interactions(s_top):
    """This function sends a cleanpipe function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"dd_intermol = cl.parse_directives_inside_intermolecular_interactions({s_top})")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_insert_text_before_directive(s_file_path, s_text_to_insert, s_directive):
    """This function sends a cleanpipe function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"cl.insert_text_before_directive({s_file_path}, {s_text_to_insert}, {s_directive})")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_replace_all_lines_of_directive(s_top_file, s_directive, ll_lines_to_add,directive_position, s_top_file_out):
    """This function sends a cleanpipe function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"cl.replace_all_lines_of_directive({s_top_file}, {s_top_file_out}, {s_directive}, {ll_lines_to_add}, {directive_position})")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_add_lines_at_the_end_of_directive(s_top_file, s_directive, ll_lines_to_add, directive_position, s_top_file_out):
    """This function sends a cleanpipe function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"cl.add_lines_at_the_end_of_directive({s_top_file}, {s_top_file_out}, {s_directive}, {ll_lines_to_add}, {directive_position})")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_put_lines_at_the_proper_place_of_directive(s_file_to_be_edited, s_directive, ll_replacement, s_out_file_name):
    """This function sends a cleanpipe function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"cl.put_lines_at_the_proper_place_of_directive({s_file_to_be_edited}, {s_out_file_name}, {s_directive}, {ll_replacement})")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_replaceMoleculeName(top_filename, old_molecule_name, new_molecule_name):
    """This function sends a cleanpipe function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"cl.replaceMoleculeName({top_filename}, {old_molecule_name}, {new_molecule_name})")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_update_molecule_quantity(top_file, molecule_name, new_quantity):
    """This function sends a cleanpipe function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"cl.update_molecule_quantity({top_file}, {molecule_name}, {new_quantity})")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_setSystemName(top_filename, new_system_name):
    """This function sends a cleanpipe function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"cl.setSystemName({top_filename}, {new_system_name})")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_replaceWordInsideDirective(top_filename, target_directive, old_word, new_word):
    """This function sends a cleanpipe function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"cl.replaceWordInsideDirective({top_filename}, {target_directive}, {old_word}, {new_word})")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"







def clipboard_include_all_itps(s_top, s_option):
    """This function sends a cleanpipe function with arguments to the clipboard."""
    
    # Copy text to the clipboard, depending on option
    if s_option == "option 1: text output":
        pyperclip.copy(f"s_expanded_includes = cl.expand_includes({s_top})")
    elif s_option == "option 2: temp file output":
        pyperclip.copy(f"s_temp_file_name = cl.expand_includes_to_temp_file({s_top})")
    else:
        raise ValueError("Invalid value for s_option")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"




def clipboard_deconstruct_top_into_molecules(s_top):
    """This function sends a cleanpipe function with arguments to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"d_created_itps = cl.deconstruct_top_into_molecules({s_top})")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"



def call_open_vmd_with_socket():
    """This function calls a function in cleanpipe directly"""
    import cleanpipe as cl

    # call function
    cl.open_vmd_with_socket()


    return "cl.open_vmd_with_socket() was called directly"












def send_tcl_to_VMD_default_cartoon_and_licorice():
    """This function sends a tcl script to a VMD with open socket"""

    import cleanpipe as cl
    
    script_name = "default_cartoon_and_licorice.tcl"

    #get where cleanpipe is, because the scripts are in a folder there
    module_path = Path(cl.__file__)
    module_dir = module_path.parent
    #cuild the script full path
    script_path = module_dir / "tcl" / script_name
    # Convert path to a string with OS-specific formatting (safe for both Windows and Linux)
    script_path_str = str(script_path)
    # convert to POSIX-style (slashes). good for windows. VMD accepts both styles but prefers forward slashes
    script_path_str = script_path.as_posix()

    # Send to VMD
    final_command = f'source "{script_path_str}"'
    cl.send_command_to_vmd(final_command)

    return f'command "{final_command}" sent to VMD'


def send_tcl_to_VMD_goodsell_blob():
    """This function sends a tcl script to a VMD with open socket"""

    import cleanpipe as cl
    
    script_name = "goodsell_blob.tcl"

    #get where cleanpipe is, because the scripts are in a folder there
    module_path = Path(cl.__file__)
    module_dir = module_path.parent
    #cuild the script full path
    script_path = module_dir / "tcl" / script_name
    # Convert path to a string with OS-specific formatting (safe for both Windows and Linux)
    script_path_str = str(script_path)
    # convert to POSIX-style (slashes). good for windows. VMD accepts both styles but prefers forward slashes
    script_path_str = script_path.as_posix()

    # Send to VMD
    final_command = f'source "{script_path_str}"'
    cl.send_command_to_vmd(final_command)

    return f'command "{final_command}" sent to VMD'

def send_tcl_to_VMD_chewing_gum():
    """This function sends a tcl script to a VMD with open socket"""

    import cleanpipe as cl
    
    script_name = "chewing_gum.tcl"

    #get where cleanpipe is, because the scripts are in a folder there
    module_path = Path(cl.__file__)
    module_dir = module_path.parent
    #cuild the script full path
    script_path = module_dir / "tcl" / script_name
    # Convert path to a string with OS-specific formatting (safe for both Windows and Linux)
    script_path_str = str(script_path)
    # convert to POSIX-style (slashes). good for windows. VMD accepts both styles but prefers forward slashes
    script_path_str = script_path.as_posix()

    # Send to VMD
    final_command = f'source "{script_path_str}"'
    cl.send_command_to_vmd(final_command)

    return f'command "{final_command}" sent to VMD'

def send_tcl_to_VMD_secondary_structure():
    """This function sends a tcl script to a VMD with open socket"""

    import cleanpipe as cl
    
    script_name = "secondary_structure.tcl"

    #get where cleanpipe is, because the scripts are in a folder there
    module_path = Path(cl.__file__)
    module_dir = module_path.parent
    #cuild the script full path
    script_path = module_dir / "tcl" / script_name
    # Convert path to a string with OS-specific formatting (safe for both Windows and Linux)
    script_path_str = str(script_path)
    # convert to POSIX-style (slashes). good for windows. VMD accepts both styles but prefers forward slashes
    script_path_str = script_path.as_posix()

    # Send to VMD
    final_command = f'source "{script_path_str}"'
    cl.send_command_to_vmd(final_command)

    return f'command "{final_command}" sent to VMD'


def send_tcl_to_VMD_eletrostatic_surface(s_users_choice_1,s_users_choice_2):
    """This function sends a tcl script to a VMD with open socket"""

    import cleanpipe as cl
    
    script_name = "eletrostatic_surface.tcl"

    #get where cleanpipe is, because the scripts are in a folder there
    module_path = Path(cl.__file__)
    module_dir = module_path.parent
    #cuild the script full path
    script_path = module_dir / "tcl" / script_name
    # Convert path to a string with OS-specific formatting (safe for both Windows and Linux)
    script_path_str = str(script_path)
    # convert to POSIX-style (slashes). good for windows. VMD accepts both styles but prefers forward slashes
    script_path_str = script_path.as_posix()

    # define the fill path and name of a temporary script, that will be created in the same directory
    dir_name = os.path.dirname(script_path_str)
    tmp_script_path_str = os.path.join(dir_name, f"eletrostatic_surface-temp_script_with_substituition_.tcl")



    # Run sed to change the keywords
    subprocess.run(f"sed 's#SED_WILL_REPLACE_THIS_1#{s_users_choice_1}#g' {script_path_str} > {tmp_script_path_str}", shell=True, check=True)
    subprocess.run(f"sed -i 's#SED_WILL_REPLACE_THIS_2#{s_users_choice_2}#g' {tmp_script_path_str}", shell=True, check=True)


    # Send to VMD
    final_command = f'source "{tmp_script_path_str}"'
    cl.send_command_to_vmd(final_command)

    #remove temporary script with the substituted keyword
    os.remove(tmp_script_path_str)

    return f'command "{final_command}" sent to VMD'


def send_tcl_to_VMD_orbital():
    """This function sends a tcl script to a VMD with open socket"""

    import cleanpipe as cl
    
    script_name = "orbital.tcl"

    #get where cleanpipe is, because the scripts are in a folder there
    module_path = Path(cl.__file__)
    module_dir = module_path.parent
    #cuild the script full path
    script_path = module_dir / "tcl" / script_name
    # Convert path to a string with OS-specific formatting (safe for both Windows and Linux)
    script_path_str = str(script_path)
    # convert to POSIX-style (slashes). good for windows. VMD accepts both styles but prefers forward slashes
    script_path_str = script_path.as_posix()


    # define the fill path and name of a temporary script, that will be created in the same directory
    dir_name = os.path.dirname(script_path_str)
    #tmp_script_path_str = os.path.join(dir_name, f"orbital-temp_script_with_substituition_.tcl")
    script_path_str = os.path.join(dir_name, f"orbital.tcl")


    # Run sed to change the keywords
    #subprocess.run(f"sed 's#SED_WILL_REPLACE_THIS_1#{s_users_choice_1}#g' {script_path_str} > {tmp_script_path_str}", shell=True, check=True)

    # Run sed to change the keywords
    #subprocess.run(
    #    ["sed", f"s#SED_WILL_REPLACE_THIS_1#{s_users_choice_1}#g", str(script_path_str)],
    #    check=True,
    #    stdout=open(tmp_script_path_str, "w"),
    #)

    # Send to VMD
    final_command = f'source "{script_path_str}"'
    cl.send_command_to_vmd(final_command)

    #remove temporary script with the substituted keyword
    #os.remove(script_path_str)

    return f'command "{final_command}" sent to VMD'


def send_tcl_to_VMD_fobic_are_yellow_and_philic_are_purple():
    """This function sends a tcl script to a VMD with open socket"""

    import cleanpipe as cl
    
    script_name = "fobic_are_yellow_and_philic_are_purple.tcl"

    #get where cleanpipe is, because the scripts are in a folder there
    module_path = Path(cl.__file__)
    module_dir = module_path.parent
    #cuild the script full path
    script_path = module_dir / "tcl" / script_name
    # Convert path to a string with OS-specific formatting (safe for both Windows and Linux)
    script_path_str = str(script_path)
    # convert to POSIX-style (slashes). good for windows. VMD accepts both styles but prefers forward slashes
    script_path_str = script_path.as_posix()

    # Send to VMD
    final_command = f'source "{script_path_str}"'
    cl.send_command_to_vmd(final_command)

    return f'command "{final_command}" sent to VMD'


def send_tcl_to_VMD_hbond_between_proteins_and_solvent():
    """This function sends a tcl script to a VMD with open socket"""

    import cleanpipe as cl
    
    script_name = "hbond_between_proteins_and_solvent.tcl"

    #get where cleanpipe is, because the scripts are in a folder there
    module_path = Path(cl.__file__)
    module_dir = module_path.parent
    #cuild the script full path
    script_path = module_dir / "tcl" / script_name
    # Convert path to a string with OS-specific formatting (safe for both Windows and Linux)
    script_path_str = str(script_path)
    # convert to POSIX-style (slashes). good for windows. VMD accepts both styles but prefers forward slashes
    script_path_str = script_path.as_posix()

    # Send to VMD
    final_command = f'source "{script_path_str}"'
    cl.send_command_to_vmd(final_command)

    return f'command "{final_command}" sent to VMD'




def call_see_interactions(s_top, s_gro, s_mol_name):
    """This function calls a function in cleanpipe directly"""

    import cleanpipe as cl
    
    # call function
    cl.see_interactions(s_top, s_gro, s_mol_name)

    return f"cl.see_interactions({s_top}, {s_gro}, {s_mol_name}) was called directly"


def call_see_partial_charges(s_itp, s_gro):
    """This function calls a function in cleanpipe directly"""

    import cleanpipe as cl
    
    # call function
    cl.see_partial_charges_from_itp(s_gro, s_itp)

    return f"cl.see_partial_charges_from_itp({s_gro}, {s_itp}) was called directly"


#def forces_in_trr():



def send_tcl_to_VMD_MARTINI_jackson():
    """This function sends a tcl script to a VMD with open socket"""

    import cleanpipe as cl
    
    script_name = "MARTINI_jackson.tcl"

    #get where cleanpipe is, because the scripts are in a folder there
    module_path = Path(cl.__file__)
    module_dir = module_path.parent
    #cuild the script full path
    script_path = module_dir / "tcl" / script_name
    # Convert path to a string with OS-specific formatting (safe for both Windows and Linux)
    script_path_str = str(script_path)
    # convert to POSIX-style (slashes). good for windows. VMD accepts both styles but prefers forward slashes
    script_path_str = script_path.as_posix()

    # Send to VMD
    final_command = f'source "{script_path_str}"'
    cl.send_command_to_vmd(final_command)

    return f'command "{final_command}" sent to VMD'


def send_tcl_to_VMD_MARTINI_henrique():
    """This function sends a tcl script to a VMD with open socket"""

    import cleanpipe as cl
    
    script_name = "MARTINI_henrique.tcl"

    #get where cleanpipe is, because the scripts are in a folder there
    module_path = Path(cl.__file__)
    module_dir = module_path.parent
    #cuild the script full path
    script_path = module_dir / "tcl" / script_name
    # Convert path to a string with OS-specific formatting (safe for both Windows and Linux)
    script_path_str = str(script_path)
    # convert to POSIX-style (slashes). good for windows. VMD accepts both styles but prefers forward slashes
    script_path_str = script_path.as_posix()

    # Send to VMD
    final_command = f'source "{script_path_str}"'
    cl.send_command_to_vmd(final_command)

    return f'command "{final_command}" sent to VMD'


def send_tcl_to_VMD_MARTINI_brasnett():
    """This function sends a tcl script to a VMD with open socket"""

    import cleanpipe as cl
    
    script_name = "MARTINI_brasnett.tcl"

    #get where cleanpipe is, because the scripts are in a folder there
    module_path = Path(cl.__file__)
    module_dir = module_path.parent
    #cuild the script full path
    script_path = module_dir / "tcl" / script_name
    # Convert path to a string with OS-specific formatting (safe for both Windows and Linux)
    script_path_str = str(script_path)
    # convert to POSIX-style (slashes). good for windows. VMD accepts both styles but prefers forward slashes
    script_path_str = script_path.as_posix()

    # Send to VMD
    final_command = f'source "{script_path_str}"'
    cl.send_command_to_vmd(final_command)

    return f'command "{final_command}" sent to VMD'


def send_tcl_to_VMD_MARTINI_bylipidtype():
    """This function sends a tcl script to a VMD with open socket"""

    import cleanpipe as cl
    
    script_name = "MARTINI_bylipidtype.tcl"

    #get where cleanpipe is, because the scripts are in a folder there
    module_path = Path(cl.__file__)
    module_dir = module_path.parent
    #cuild the script full path
    script_path = module_dir / "tcl" / script_name
    # Convert path to a string with OS-specific formatting (safe for both Windows and Linux)
    script_path_str = str(script_path)
    # convert to POSIX-style (slashes). good for windows. VMD accepts both styles but prefers forward slashes
    script_path_str = script_path.as_posix()

    # Send to VMD
    final_command = f'source "{script_path_str}"'
    cl.send_command_to_vmd(final_command)

    return f'command "{final_command}" sent to VMD'


def send_tcl_to_VMD_MARTINI_bylipid_blue_red(s_users_choice):
    """This function sends a tcl script to a VMD with open socket"""


    
    script_name = "MARTINI_bylipid_blue_red.tcl"

    #get where cleanpipe is, because the scripts are in a folder there
    module_path = Path(cl.__file__)
    module_dir = module_path.parent
    #build the script full path
    script_path = module_dir / "tcl" / script_name
    # Convert path to a string with OS-specific formatting (safe for both Windows and Linux)
    script_path_str = str(script_path)
    # convert to POSIX-style (slashes). good for windows. VMD accepts both styles but prefers forward slashes
    script_path_str = script_path.as_posix()





    # define the fill path and name of a temporary script, that will be created in the same directory
    dir_name = os.path.dirname(script_path_str)
    tmp_script_path_str = os.path.join(dir_name, f"MARTINI_bylipid_blue_red-temp_script_with_substituition_.tcl")


    # Run sed to change the keyword replace_this
    subprocess.run(f"sed 's/SED_WILL_REPLACE_THIS/{s_users_choice}/g' {script_path_str} > {tmp_script_path_str}", shell=True, check=True)

    # Send to VMD
    final_command = f'source "{tmp_script_path_str}"'
    cl.send_command_to_vmd(final_command)

    #remove temporary script with the substituted keyword
    os.remove(tmp_script_path_str)

    return f'command "{final_command}" sent to VMD'


def send_tcl_to_VMD_MARTINI_bylipid_bighead_smallhead():
    """This function sends a tcl script to a VMD with open socket"""

    import cleanpipe as cl
    
    script_name = "MARTINI_bylipid_bighead_smallhead.tcl"

    #get where cleanpipe is, because the scripts are in a folder there
    module_path = Path(cl.__file__)
    module_dir = module_path.parent
    #cuild the script full path
    script_path = module_dir / "tcl" / script_name
    # Convert path to a string with OS-specific formatting (safe for both Windows and Linux)
    script_path_str = str(script_path)
    # convert to POSIX-style (slashes). good for windows. VMD accepts both styles but prefers forward slashes
    script_path_str = script_path.as_posix()

    # Send to VMD
    final_command = f'source "{script_path_str}"'
    cl.send_command_to_vmd(final_command)

    return f'command "{final_command}" sent to VMD'


def send_tcl_to_VMD_MARTINI_bylipid_solid_liquid():
    """This function sends a tcl script to a VMD with open socket"""

    import cleanpipe as cl
    
    script_name = "MARTINI_bylipid_solid_liquid.tcl"

    #get where cleanpipe is, because the scripts are in a folder there
    module_path = Path(cl.__file__)
    module_dir = module_path.parent
    #cuild the script full path
    script_path = module_dir / "tcl" / script_name
    # Convert path to a string with OS-specific formatting (safe for both Windows and Linux)
    script_path_str = str(script_path)
    # convert to POSIX-style (slashes). good for windows. VMD accepts both styles but prefers forward slashes
    script_path_str = script_path.as_posix()

    # Send to VMD
    final_command = f'source "{script_path_str}"'
    cl.send_command_to_vmd(final_command)

    return f'command "{final_command}" sent to VMD'


def send_tcl_to_VMD_MARTINI_technical():
    """This function sends a tcl script to a VMD with open socket"""

    import cleanpipe as cl
    
    script_name = "MARTINI_technical.tcl"

    #get where cleanpipe is, because the scripts are in a folder there
    module_path = Path(cl.__file__)
    module_dir = module_path.parent
    #cuild the script full path
    script_path = module_dir / "tcl" / script_name
    # Convert path to a string with OS-specific formatting (safe for both Windows and Linux)
    script_path_str = str(script_path)
    # convert to POSIX-style (slashes). good for windows. VMD accepts both styles but prefers forward slashes
    script_path_str = script_path.as_posix()

    # Send to VMD
    final_command = f'source "{script_path_str}"'
    cl.send_command_to_vmd(final_command)

    return f'command "{final_command}" sent to VMD'


def send_tcl_to_VMD_MARTINI_cg_bonds(s_top_full_path):
    """This function sends a tcl script to a VMD with open socket"""

    import cleanpipe as cl
    
    script_name = "cg_bonds-v6.tcl"

    #get where cleanpipe is, because the scripts are in a folder there
    module_path = Path(cl.__file__)
    module_dir = module_path.parent
    #cuild the script full path
    script_path = module_dir / "tcl" / script_name
    # Convert path to a string with OS-specific formatting (safe for both Windows and Linux)
    script_path_str = str(script_path)
    # convert to POSIX-style (slashes). good for windows. VMD accepts both styles but prefers forward slashes
    script_path_str = script_path.as_posix()

    # Send to VMD
    final_command = f'source "{script_path_str}"'
    cl.send_command_to_vmd(final_command)

    #############################################################################
    # after sourcing, Ill send some commands that are particular to that script #
    #############################################################################

    s_base = cl.get_file_location(s_top_full_path)
    s_name = cl.get_filename_with_extension(s_top_full_path)


    cl.send_command_to_vmd(r"pwd")
    cl.send_command_to_vmd(f"cd {s_base}")
    cl.send_command_to_vmd(r"pwd")


    # cg_bonds -top ./dspc.top -topoltype "elastic"
    cl.send_command_to_vmd(f"cg_bonds -top ./{s_name} -topoltype \"elastic\"")

    # alternative that makes it beautiful, but it requires a tpr and I have my ways of making it beautiful
    # cg_bonds -gmx /home/hrigitano/miniconda3/envs/bio/bin.AVX2_256/gmx -tpr ./dspc-md.tpr -net "elastic" -cutoff 12.0 -color "orange" -mat "AOChalky" -res 12 -rad 0.1 -topoltype "elastic"
    #cl.send_command_to_vmd(r"cg_bonds -tpr /data1/henrique/martinitutorial/bilayer-lipidome-tutorial-I/minimal/spontaneous-assembly/phase_sep.tpr -gmx /home/hrigitano/miniconda3/envs/bio/bin.AVX2_256/gmx")

    # these are not normal representations. to delete them, use:
    # cg_delete_all_graphics

    return f'a tcl script and some commands were sent to VMD'


def send_tcl_to_VMD_MARTINI_cg_bonds_delete():
    """This function sends a tcl script to a VMD with open socket"""

    import cleanpipe as cl
    

    final_command = f'cg_delete_all_graphics'
    cl.send_command_to_vmd(final_command)



    return f'a couple of commands were sent to VMD'


def send_tcl_to_VMD_selection_highlight(s_users_choice_1,s_users_choice_2,s_users_choice_3,s_users_choice_4):
    """This function sends a tcl script to a VMD with open socket"""

    import cleanpipe as cl
    import subprocess
    
    script_name = "selection_highlight.tcl"

    #get where cleanpipe is, because the scripts are in a folder there
    module_path = Path(cl.__file__)
    module_dir = module_path.parent
    #cuild the script full path
    script_path = module_dir / "tcl" / script_name
    # Convert path to a string with OS-specific formatting (safe for both Windows and Linux)
    script_path_str = str(script_path)
    # convert to POSIX-style (slashes). good for windows. VMD accepts both styles but prefers forward slashes
    script_path_str = script_path.as_posix()






    # define the fill path and name of a temporary script, that will be created in the same directory
    dir_name = os.path.dirname(script_path_str)
    tmp_script_path_str = os.path.join(dir_name, f"selection_highlight-temp_script_with_substituition_.tcl")


    # Run sed to change the keywords
    subprocess.run(f"sed 's/SED_WILL_REPLACE_THIS_1/{s_users_choice_1}/g' {script_path_str} > {tmp_script_path_str}", shell=True, check=True)
    subprocess.run(f"sed -i 's/SED_WILL_REPLACE_THIS_2/{s_users_choice_2}/g' {tmp_script_path_str}", shell=True, check=True)
    subprocess.run(f"sed -i 's/SED_WILL_REPLACE_THIS_3/{s_users_choice_3}/g' {tmp_script_path_str}", shell=True, check=True)
    subprocess.run(f"sed -i 's/SED_WILL_REPLACE_THIS_4/{s_users_choice_4}/g' {tmp_script_path_str}", shell=True, check=True)




    # Send to VMD
    final_command = f'source "{tmp_script_path_str}"'
    cl.send_command_to_vmd(final_command)

    #remove temporary script with the substituted keyword
    os.remove(tmp_script_path_str)

    return f'command "{final_command}" sent to VMD'


def send_tcl_to_VMD_inspect_file():
    """This function sends a tcl script to a VMD with open socket"""

    import cleanpipe as cl
    
    script_name = "inspect_file.tcl"

    #get where cleanpipe is, because the scripts are in a folder there
    module_path = Path(cl.__file__)
    module_dir = module_path.parent
    #cuild the script full path
    script_path = module_dir / "tcl" / script_name
    # Convert path to a string with OS-specific formatting (safe for both Windows and Linux)
    script_path_str = str(script_path)
    # convert to POSIX-style (slashes). good for windows. VMD accepts both styles but prefers forward slashes
    script_path_str = script_path.as_posix()

    # Send to VMD
    final_command = f'source "{script_path_str}"'
    cl.send_command_to_vmd(final_command)

    return f'command "{final_command}" sent to VMD'


def call_align_using_selected_atoms():
    """This function calls a function in cleanpipe directly"""

    import cleanpipe as cl
    
    # call function
    cl.align_using_selected_atoms()

    return "cl.align_using_selected_atoms() was called directly"


def call_load_files_into_vmd_frames(s_full_path_with_spetial_char):
    """This function calls a function in cleanpipe directly"""

    import cleanpipe as cl
    
    # call function
    cl.load_files_into_vmd_frames(s_full_path_with_spetial_char.strip())

    return "cl.load_files_into_vmd_frames() was called directly"


def call_create_gif_from_vmd_frames(s_out_folder,s_duration):
    """This function calls a function in cleanpipe directly"""

    import cleanpipe as cl

    n_duration = int(s_duration.strip())
    
    # call function
    cl.create_gif_from_vmd_frames()

    return "cl.create_gif_from_vmd_frames() was called directly"



def clipboard_ns_for_all_lambdas(s_folder):
    """This function sends this text to the clipboard.
    
    for i in $(seq -w 0 20); do for LEG in O W; do XTC=( jayCHYO-transfer/*${LEG}__runFEP/t*/Lambda_${i}/4_PROD/*${LEG}_prod_*${i}.all.xtc ); if [ ! -f "${XTC[0]}" ]; then printf "Lambda_%-4s %-3s MISSING\n" "${i}" "${LEG}"; else LAST=$(python3 -c "
    import struct, sys
    f=open('${XTC[0]}','rb')
    t=0
    while True:
        hdr=f.read(92)
        if len(hdr)<92: break
        magic,natoms,step=struct.unpack('>iii',hdr[:12])
        t=struct.unpack('>f',hdr[12:16])[0]
        size=struct.unpack('>i',hdr[88:92])[0]
        size=((size+3)//4)*4
        f.seek(size,1)
    f.close()
    print(t)
    " 2>/dev/null); [ -z "$LAST" ] && printf "Lambda_%-4s %-3s ERROR\n" "${i}" "${LEG}" || printf "Lambda_%-4s %-3s %.1f ns\n" "${i}" "${LEG}" "$(LC_ALL=C awk "BEGIN{print $LAST/1000}")"; fi; done; done
        
    """
    
    # Copy text to the clipboard
    pyperclip.copy(f'for i in $(seq -w 0 20); do for LEG in O W; do XTC=( {s_folder}/*${{LEG}}__runFEP/t*/Lambda_${{i}}/4_PROD/*${{LEG}}_prod_*${{i}}.all.xtc ); if [ ! -f "${{XTC[0]}}" ]; then printf "Lambda_%-4s %-3s MISSING\\n" "${{i}}" "${{LEG}}"; else LAST=$(python3 -c "\nimport struct, sys\nf=open(\'${{XTC[0]}}\',\'rb\')\nt=0\nwhile True:\n    hdr=f.read(92)\n    if len(hdr)<92: break\n    magic,natoms,step=struct.unpack(\'>iii\',hdr[:12])\n    t=struct.unpack(\'>f\',hdr[12:16])[0]\n    size=struct.unpack(\'>i\',hdr[88:92])[0]\n    size=((size+3)//4)*4\n    f.seek(size,1)\nf.close()\nprint(t)\n" 2>/dev/null); [ -z "$LAST" ] && printf "Lambda_%-4s %-3s ERROR\\n" "${{i}}" "${{LEG}}" || printf "Lambda_%-4s %-3s %.1f ns\\n" "${{i}}" "${{LEG}}" "$(LC_ALL=C awk "BEGIN{{print $LAST/1000}}")"; fi; done; done')

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"



def clipboard_Delta_E_off(s_folder):
    """This function sends a text to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f'DIR="{s_folder}"; find "$DIR" -type f -name \'*barint*.xvg\' -path \'*bar*\' -print0 | while IFS= read -r -d \'\' f; do awk \'END{{if($1==20) printf "%s  %.6f\\n", FILENAME, $2*-2.47}}\' "$f"; done')


    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_Delta_E_Transfer_OtoW(s_folder):
    """This function sends a text to the clipboard."""
    
    # Copy text to the clipboard
    pyperclip.copy(f"DIR=\"{s_folder}\"; O=$(find \"$DIR\" -type f -name '*barint*.xvg' -path '*O*' -print -quit | xargs tail -n1 | awk '$1==20{{print $2}}'); W=$(find \"$DIR\" -type f -name '*barint*.xvg' -path '*W*' -print -quit | xargs tail -n1 | awk '$1==20{{print $2}}'); awk -v O=\"$O\" -v W=\"$W\" 'BEGIN {{ print W*-2.47 - O*-2.47 }}'")

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_gro_scan(s_option, s_gro, s_top, s_i, s_j, s_k, s_l, s_output_folder):
    """This function sends a text to the clipboard."""

    pyperclip.copy(f"./dihedral_scan_gromacs.sh -g {s_gro} -p {s_top} -i {s_i} -j {s_j} -k {s_k} -l {s_l} -o {s_output_folder}")

    
    sent = pyperclip.paste()
    return sent + " sent to clipboard"


def clipboard_collect_optimized_gromacs_scan(s_out_folder_name):
    """This function sends a text to the clipboard."""

    pyperclip.copy(f"d_gro_scan = cl.collect_optimized_gromacs_scan('{s_out_folder_name}')")

    
    sent = pyperclip.paste()
    return sent + " sent to clipboard"


def clipboard_rama(s_option):
    """This function sends a text to the clipboard."""
    
    if s_option == "calculate":
        pyperclip.copy(f'cl.calc_rama("xtcs/lC_inW_prod_298_00.all.xtc", "../collected_tprs/lC_inW_prod_298_00.tpr","lC_inW_rama",b_overwrite=False)')
    elif s_option == "plot":
        pyperclip.copy(f'cl.plot_rama("rama/lC_inW_rama.csv","peptide in water")')
        
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_dssp(s_option):
    """This function sends a text to the clipboard."""
    
    if s_option == "calculate":
        pyperclip.copy(f'cl.calc_dssp("xtcs/lC_inO_prod_298_00.all.xtc", "../lC_inO__runFEP/t298/Lambda_00/3_NPT/lC_inO_npt.gro", "lC_inO_dssp_298_00",b_overwrite=False)')
    elif s_option == "plot":
        pyperclip.copy(f'cl.plot_dssp("dssp/lC_inO_dssp_298_00.dat","peptide in octane")')
        

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_sasa(s_option):
    """This function sends a text to the clipboard."""
    
    if s_option == "calculate":
        pyperclip.copy(f'cl.calc_sasa("xtcs/lC_inW_prod_298_00.all.xtc", "../collected_tprs/lC_inW_prod_298_00.tpr","lC_inW_prod_298_00_sasa",b_overwrite=False)')
    elif s_option == "plot":
        pyperclip.copy(f'cl.plot_sasa("sasa/lC_inW_prod_298_00_sasa.xvg","Solvent Accessible Surface Area over Time\\npeptide in water")')
        

    # Retrieve text from the clipboard
    sent = pyperclip.paste()

    return sent + " sent to clipboard"


def clipboard_train_test_plit():
    """This function sends a text to the clipboard."""
    
    pyperclip.copy(
        f"""x_df = df.loc[:, df.columns != 'Name of target column']
y_df = df['Name of target column']
x_train, x_test, y_train, y_test = train_test_split(x_df,y_df, random_state=7, test_size=0.3)"""
    )

    sent = pyperclip.paste()
    return sent + " sent to clipboard"


def clipboard_create_psi4_molecule(s_user_choice):
    """This function sends a text to the clipboard."""
    
    if s_user_choice == "hardcode from scratch":
        pyperclip.copy(f"""
mymol = psi4.geometry(\"\"\"
   O        1.16530       -0.83090       -0.09560
   O        2.30590        0.82840        1.03690
   C       -0.11050       -0.34740        0.31060
   C       -0.41500        0.96500       -0.41070
   C       -1.17480       -1.40610        0.02570
   C       -1.81480        1.47410       -0.08260
   C       -2.57460       -0.89720        0.35390
   C       -2.87820        0.41540       -0.36490
   C        2.21840        0.01020        0.13140
   C        3.27830       -0.21150       -0.90470
   H       -0.08640       -0.17470        1.39510
   H       -0.31790        0.81940       -1.49470
   H        0.30560        1.74810       -0.15280
   H       -0.95860       -2.31360        0.60210
   H       -1.12360       -1.70550       -1.02920
   H       -2.02750        2.37460       -0.66970
   H       -1.85950        1.76330        0.97460
   H       -2.66420       -0.74880        1.43710
   H       -3.31720       -1.65210        0.07240
   H       -3.86060        0.78760       -0.05330
   H       -2.93300        0.23400       -1.44540
   H        2.87470        0.00080       -1.89800
   H        3.64220       -1.24040       -0.84830
   H        4.11630        0.46580       -0.71700
\"\"\")   
        """)

    elif s_user_choice == "from gro file":
        pyperclip.copy(f"mol_object = cl.gro2psi4_object('foo/bar.gro', charge=0, multiplicity=1)")

    elif s_user_choice == "from xyz file":
        pyperclip.copy(f"mol_object = cl.xyz2psi4_object('foo/bar.xyz', charge=0, multiplicity=1)")



    

    sent = pyperclip.paste()
    return sent + " sent to clipboard"



def clipboard_see_psi4_molecule(s_molname):
    """This function sends a text to the clipboard."""
    
    pyperclip.copy(f"cl.see_labeled_molecule({s_molname})")

    sent = pyperclip.paste()
    return sent + " sent to clipboard"


def clipboard_reorder_psi4_molecule(s_molname,s_dictname):
    """This function sends a text to the clipboard."""
    
    pyperclip.copy(f"reordered = cl.reorder_psi4_molecule({s_molname},{s_dictname})")

    sent = pyperclip.paste()
    return sent + " sent to clipboard"


def clipboard_psi2xyz(s_input,s_output):
    """This function sends a text to the clipboard."""
    
    pyperclip.copy(f"{s_input}.save_xyz_file('{s_output}', True)")

    sent = pyperclip.paste()
    return sent + " sent to clipboard"



def clipboard_xyz2GroPdbXyz_WithDefinedDihedral(s_input,s_output,s_dihedral_definition, s_list_of_angles):
    """This function sends a text to the clipboard."""
    
    pyperclip.copy(f"cl.xyz2multiple_formats_with_defined_dihedral('{s_input}', {s_dihedral_definition}, angles={s_list_of_angles}, out_folder='{s_output}')")

    sent = pyperclip.paste()
    return sent + " sent to clipboard"


def clipboard_qm_energy(s_user_choice,s_basis,s_out_folder):
    """This function sends a text to the clipboard."""
    
    pyperclip.copy(f'energy, wfn = cl.qm_energy(water, "{s_user_choice}", "{s_basis}", "{s_out_folder}", b_optimize=True)')

    sent = pyperclip.paste()
    return sent + " sent to clipboard"


def clipboard_scan(s_option, s_molname, s_ids, s_out_folder_name):
    """This function sends a text to the clipboard."""

    if s_option == "bond":
        pyperclip.copy(f"cl.qm_bond_scan({s_molname},{s_ids}, s_out_folder_name='{s_out_folder_name}')")
    elif s_option == "angle":
        pyperclip.copy(f"cl.qm_angle_scan({s_molname},{s_ids}, s_out_folder_name='{s_out_folder_name}')")
    elif s_option == "dihedral":
        pyperclip.copy(f"cl.qm_dihedral_scan({s_molname},{s_ids}, s_out_folder_name='{s_out_folder_name}')")
    
    
    sent = pyperclip.paste()
    return sent + " sent to clipboard"


def clipboard_collect_optimized_qm_scan(s_out_folder_name):
    """This function sends a text to the clipboard."""

    pyperclip.copy(f"d_qm_scan = cl.collect_optimized_qm_scan('{s_out_folder_name}')")

    
    sent = pyperclip.paste()
    return sent + " sent to clipboard"


def clipboard_qm_checks(s_option):
    """This function sends a text to the clipboard."""

    if s_option == "check 1 (psi slices by order)":
        pyperclip.copy(f'cl.cubes_check1("results/Psi_a_38_38-A.cube")')
    elif s_option == "check 2 (density isosurface with ESP)":
        pyperclip.copy(f'cl.cubes_check2("results/Dt.cube", "results/ESP.cube")')
    elif s_option == "check 3 (ESP histogram)":
        pyperclip.copy(f'cl.cubes_check3("results/ESP.cube")')
    
    
    sent = pyperclip.paste()
    return sent + " sent to clipboard"


def clipboard_trim_ESP():
    """This function sends a text to the clipboard."""


    pyperclip.copy(f'cl.trim_cube("results/ESP.cube", "results/ESP_trimmed.cube", vmin=-0.12, vmax=0.05)')

    sent = pyperclip.paste()
    return sent + " sent to clipboard"

def clipboard_cc_fit(s_option):
    """This function sends a text to the clipboard."""


    if s_option == "straight line":
        pyperclip.copy(f'cl.continuous_continuous_linearRegression(x, y)')
    elif s_option == "exponential":
        pyperclip.copy(f'cl.continuous_continuous_nonlinearRegression(x, y, MODEL="exponential")')
    elif s_option == "polinomial":
        pyperclip.copy(f'cl.continuous_continuous_nonlinearRegression(x, y, MODEL="polinomial")')
    elif s_option == "sinusoidal":
        pyperclip.copy(f'cl.continuous_continuous_nonlinearRegression(x, y, MODEL="sinusoidal")')
    elif s_option == "fourrier (dihedral type 5)":
        pyperclip.copy(f'cl.fit_constrained_fourier(x, y)')
    elif s_option == "1+cos (dihedral type 9)":
        pyperclip.copy(f'cl.fit_gromacs_type9_multi(phi_deg,y,multiplicities)')
    

    sent = pyperclip.paste()
    return sent + " sent to clipboard"



def clipboard_cd_test(s_option):
    """This function sends a text to the clipboard."""


    if s_option == "the discrete variable has 2 categories":
        pyperclip.copy(f'cl.continuous_2categories(x, d)')
    elif s_option == "the discrete variable has MANY categories":
        pyperclip.copy(f'cl.continuous_MANYcategories(x,d)')

    
    sent = pyperclip.paste()
    return sent + " sent to clipboard"



def clipboard_dd_test():
    """This function sends a text to the clipboard."""


    pyperclip.copy(f'cl.categorica_categorical(x, y)')


    
    sent = pyperclip.paste()
    return sent + " sent to clipboard"



def clipboard_mlcontinuous(s_option):
    """This function sends a text to the clipboard."""

    if s_option == "XGBoost":
        pyperclip.copy(f'model = XGBRegressor().fit(X, y)')
    elif s_option == "decision tree":
        pyperclip.copy(f'xxxx')
    elif s_option == "naive bayes":
        pyperclip.copy(f'xxxx')
    elif s_option == "neural network":
        pyperclip.copy(f'xxxx')
    elif s_option == "multiple linear regression":
        pyperclip.copy(f'cl.multiple_linear_regression(X,y,plot = False)')

    sent = pyperclip.paste()
    return sent + " sent to clipboard"

def clipboard_mldiscrete(s_option):
    """This function sends a text to the clipboard."""

    if s_option == "XGBoost":
        pyperclip.copy(f'model = XGBClassifier().fit(X, y)')
    elif s_option == "svm":
        pyperclip.copy(f'cl.continuous_continuous_svm(ll)')
    elif s_option == "clustering - kmeans":
        pyperclip.copy(f'xxxx')
    elif s_option == "clustering - hierarchical":
        pyperclip.copy(f'xxxx')
    elif s_option == "clustering - DBSCAN":
        pyperclip.copy(f'xxxx')

    sent = pyperclip.paste()
    return sent + " sent to clipboard"
